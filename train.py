from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# ============================================================
# HANDWRITTEN DIGIT RECOGNITION USING CNN
# MNIST DATASET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "outputs"

MODEL_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "mnist_cnn.keras"


print("=" * 60)
print("HANDWRITTEN DIGIT RECOGNITION USING CNN")
print("=" * 60)


# ============================================================
# STEP 1: LOAD MNIST DATASET
# ============================================================

print("\n[1] Loading MNIST dataset...")

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


print("\nDataset Information")
print("-" * 40)
print("Training images :", len(x_train))
print("Testing images  :", len(x_test))
print("Image size      :", x_train.shape[1:])
print("Number of classes:", len(np.unique(y_train)))


# ============================================================
# STEP 2: PREPROCESS DATA
# ============================================================

print("\n[2] Preprocessing images...")

# Convert pixel values from 0-255 to 0-1
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Add channel dimension
# 28 x 28 becomes 28 x 28 x 1
x_train = np.expand_dims(x_train, axis=-1)
x_test = np.expand_dims(x_test, axis=-1)


print("Training shape:", x_train.shape)
print("Testing shape :", x_test.shape)


# ============================================================
# STEP 3: BUILD CNN MODEL
# ============================================================

print("\n[3] Building CNN model...")

model = tf.keras.Sequential([
    
    # Input layer
    tf.keras.layers.Input(shape=(28, 28, 1)),

    # First convolution
    tf.keras.layers.Conv2D(
        32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    # Reduce image size
    tf.keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Second convolution
    tf.keras.layers.Conv2D(
        64,
        kernel_size=(3, 3),
        activation="relu"
    ),

    # Reduce image size again
    tf.keras.layers.MaxPooling2D(
        pool_size=(2, 2)
    ),

    # Convert feature maps to one-dimensional vector
    tf.keras.layers.Flatten(),

    # Fully connected layer
    tf.keras.layers.Dense(
        128,
        activation="relu"
    ),

    # Prevent overfitting
    tf.keras.layers.Dropout(0.3),

    # Output layer
    # 10 neurons = digits 0 to 9
    tf.keras.layers.Dense(
        10,
        activation="softmax"
    )
])


# ============================================================
# STEP 4: COMPILE MODEL
# ============================================================

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


print("\nCNN Architecture:")
model.summary()


# ============================================================
# STEP 5: TRAIN MODEL
# ============================================================

print("\n[4] Training CNN...")
print("This may take a few minutes.\n")


history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)


# ============================================================
# STEP 6: TEST MODEL
# ============================================================

print("\n[5] Testing model using 10,000 test images...")

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)


print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Test Loss     : {test_loss:.4f}")
print(f"Test Accuracy : {test_accuracy * 100:.2f}%")

print("=" * 60)


# ============================================================
# STEP 7: SAVE MODEL
# ============================================================

model.save(MODEL_PATH)

print("\nCNN model saved successfully!")
print("Location:")
print(MODEL_PATH)


# ============================================================
# STEP 8: SAVE ACCURACY GRAPH
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.title(
    "CNN Training and Validation Accuracy"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "accuracy.png",
    dpi=150
)

plt.close()


# ============================================================
# STEP 9: SAVE LOSS GRAPH
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.title(
    "CNN Training and Validation Loss"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "loss.png",
    dpi=150
)

plt.close()


# ============================================================
# STEP 10: CONFUSION MATRIX
# ============================================================

print("\nCreating confusion matrix...")

predictions = model.predict(
    x_test,
    batch_size=256,
    verbose=0
)

predicted_labels = np.argmax(
    predictions,
    axis=1
)


cm = confusion_matrix(
    y_test,
    predicted_labels
)


display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=np.arange(10)
)


fig, ax = plt.subplots(figsize=(8, 8))

display.plot(
    ax=ax,
    values_format="d",
    colorbar=False
)

ax.set_title(
    "MNIST CNN Confusion Matrix"
)

fig.tight_layout()

fig.savefig(
    OUTPUT_DIR / "confusion_matrix.png",
    dpi=150
)

plt.close(fig)


# ============================================================
# FINISHED
# ============================================================

print("\n" + "=" * 60)
print("TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("\nGenerated files:")

print("1. models/mnist_cnn.keras")
print("2. outputs/accuracy.png")
print("3. outputs/loss.png")
print("4. outputs/confusion_matrix.png")

print("\nNext step:")
print("Run: python app.py")
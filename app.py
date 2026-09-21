from pathlib import Path
import base64
import io

import numpy as np
import tensorflow as tf

from PIL import Image, ImageOps
from flask import Flask, render_template, request, jsonify


# ============================================================
# FLASK APP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "mnist_cnn.keras"

app = Flask(__name__)


# ============================================================
# LOAD TRAINED CNN
# ============================================================

if MODEL_PATH.exists():

    print("Loading trained CNN model...")

    model = tf.keras.models.load_model(MODEL_PATH)

    print("Model loaded successfully!")

else:

    model = None

    print("ERROR: Trained model not found.")
    print("Please run the CNN training notebook first.")


# ============================================================
# PREPROCESS IMAGE FOR MNIST
# ============================================================

def preprocess_pil_image(image):
    """
    Convert an uploaded/drawn image into MNIST-style input.

    Final shape:
        (1, 28, 28, 1)
    """

    # Convert to grayscale
    image = image.convert("L")

    # Convert to numpy
    arr = np.array(image)

    # --------------------------------------------------------
    # Automatically handle white-background images
    # --------------------------------------------------------
    #
    # MNIST:
    # black background + white digit
    #
    # Uploaded image may be:
    # white background + black digit
    #
    # If background is bright, invert the image.
    # --------------------------------------------------------

    if np.mean(arr) > 127:
        arr = 255 - arr

    image = Image.fromarray(arr.astype(np.uint8))

    # --------------------------------------------------------
    # Find bounding box around digit
    # --------------------------------------------------------

    bbox = image.getbbox()

    if bbox is not None:

        image = image.crop(bbox)

    # --------------------------------------------------------
    # Add padding
    # --------------------------------------------------------

    width, height = image.size

    max_dimension = max(width, height)

    padding = int(max_dimension * 0.20)

    new_width = width + (padding * 2)
    new_height = height + (padding * 2)

    padded = Image.new(
        "L",
        (new_width, new_height),
        0
    )

    padded.paste(
        image,
        (
            padding,
            padding
        )
    )

    image = padded

    # --------------------------------------------------------
    # Resize to 28 × 28
    # --------------------------------------------------------

    image = image.resize(
        (28, 28),
        Image.Resampling.LANCZOS
    )

    # --------------------------------------------------------
    # Normalize pixels
    # --------------------------------------------------------

    arr = np.array(image).astype("float32") / 255.0

    # CNN input shape
    arr = arr.reshape(
        1,
        28,
        28,
        1
    )

    return arr


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# PREDICT FROM IMAGE
# ============================================================

def predict_image(image):

    if model is None:

        raise Exception(
            "CNN model not found. "
            "Train the model first."
        )

    # Preprocess
    processed_image = preprocess_pil_image(
        image
    )

    # CNN prediction
    probabilities = model.predict(
        processed_image,
        verbose=0
    )[0]

    # Highest probability
    predicted_digit = int(
        np.argmax(probabilities)
    )

    confidence = float(
        probabilities[predicted_digit] * 100
    )

    # Probability of all digits
    all_probabilities = [
        round(float(p) * 100, 2)
        for p in probabilities
    ]

    return {
        "digit": predicted_digit,
        "confidence": round(
            confidence,
            2
        ),
        "probabilities": all_probabilities
    }


# ============================================================
# PREDICTION ROUTE
# Supports:
# 1. Uploaded image
# 2. Canvas drawing
# ============================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # ----------------------------------------------------
        # OPTION 1: UPLOADED IMAGE
        # ----------------------------------------------------

        if "file" in request.files:

            file = request.files["file"]

            if file.filename == "":
                return jsonify({
                    "error":
                    "No image selected."
                }), 400

            image = Image.open(
                file.stream
            )

            result = predict_image(
                image
            )

            return jsonify(result)


        # ----------------------------------------------------
        # OPTION 2: CANVAS IMAGE
        # ----------------------------------------------------

        data = request.get_json(
            silent=True
        )

        if data and data.get("image"):

            image_data = data["image"]

            if "," in image_data:

                image_data = image_data.split(
                    ",",
                    1
                )[1]

            image_bytes = base64.b64decode(
                image_data
            )

            image = Image.open(
                io.BytesIO(image_bytes)
            )

            result = predict_image(
                image
            )

            return jsonify(result)


        return jsonify({
            "error":
            "No image received."
        }), 400


    except Exception as error:

        print("Prediction error:", error)

        return jsonify({
            "error":
            str(error)
        }), 400


# ============================================================
# START FLASK
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("HANDWRITTEN DIGIT RECOGNITION")
    print("=" * 60)
    print()
    print(
        "Open: http://127.0.0.1:5000"
    )
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
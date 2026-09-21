# Handwritten Digit Recognition using CNN

A web-based Handwritten Digit Recognition system that uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to recognize handwritten digits from uploaded images.

## 🚀 Features

- Upload a handwritten digit image
- Automatic digit recognition using CNN
- MNIST dataset-based model
- Prediction result displayed through a web interface
- Flask backend
- Responsive frontend
- Pre-trained Keras CNN model
- Simple and user-friendly interface

## 🧠 How It Works

The system follows these steps:

1. User uploads an image containing a handwritten digit.
2. Flask receives the uploaded image.
3. The image is preprocessed:
   - Converted to grayscale
   - Resized to 28 × 28 pixels
   - Normalized
4. The processed image is passed to the trained CNN model.
5. The CNN predicts the digit from `0` to `9`.
6. The predicted digit is displayed on the webpage.

## 🏗️ Project Architecture

```text
User
  │
  ▼
Web Interface
  │
  ▼
Flask Application
  │
  ▼
Image Preprocessing
  │
  ▼
CNN Model
  │
  ▼
Digit Prediction
  │
  ▼
Result Display



Yes — you need a **`README.md`** for the GitHub repository. Your current project has the actual application files, but a proper README will explain what the project does, how it works, how to run it, and the technologies used.

Create a file in the project root:

```text
Handwritten Digit Recognition/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md          ← create this
├── CNN_MNIST_Training.ipynb
├── train.ipynb
├── models/
│   └── mnist_cnn.keras
├── static/
│   ├── script.js
│   └── style.css
└── templates/
    └── index.html
```

Paste this into **`README.md`**:

````markdown
# Handwritten Digit Recognition using CNN

A web-based Handwritten Digit Recognition system that uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to recognize handwritten digits from uploaded images.

## 🚀 Features

- Upload a handwritten digit image
- Automatic digit recognition using CNN
- MNIST dataset-based model
- Prediction result displayed through a web interface
- Flask backend
- Responsive frontend
- Pre-trained Keras CNN model
- Simple and user-friendly interface

## 🧠 How It Works

The system follows these steps:

1. User uploads an image containing a handwritten digit.
2. Flask receives the uploaded image.
3. The image is preprocessed:
   - Converted to grayscale
   - Resized to 28 × 28 pixels
   - Normalized
4. The processed image is passed to the trained CNN model.
5. The CNN predicts the digit from `0` to `9`.
6. The predicted digit is displayed on the webpage.

## 🏗️ Project Architecture

```text
User
  │
  ▼
Web Interface
  │
  ▼
Flask Application
  │
  ▼
Image Preprocessing
  │
  ▼
CNN Model
  │
  ▼
Digit Prediction
  │
  ▼
Result Display
````

## 📁 Project Structure

```text
Handwritten-Digit-Recognition/
│
├── app.py
├── train.py
├── requirements.txt
│
├── CNN_MNIST_Training.ipynb
├── train.ipynb
│
├── models/
│   └── mnist_cnn.keras
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    └── index.html
```

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* Convolutional Neural Network (CNN)
* Flask
* NumPy
* OpenCV / PIL
* HTML
* CSS
* JavaScript
* MNIST Dataset

## 📊 Dataset

The project uses the **MNIST handwritten digit dataset**.

The dataset contains images of handwritten digits from:

```text
0 1 2 3 4 5 6 7 8 9
```

Each image is represented as a grayscale image of size:

```text
28 × 28 pixels
```

## 🧠 CNN Model

The model is trained using a Convolutional Neural Network.

A typical architecture consists of:

```text
Input Image
    ↓
Convolution Layer
    ↓
Pooling Layer
    ↓
Convolution Layer
    ↓
Pooling Layer
    ↓
Flatten
    ↓
Dense Layer
    ↓
Output Layer
    ↓
10 Classes (0–9)
```

The trained model is saved as:

```text
models/mnist_cnn.keras
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/manojtk900/Handwritten-Digit-Recognition.git
```

### 2. Navigate to the project

```bash
cd Handwritten-Digit-Recognition
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv env
```

Activate it:

```bash
env\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

## 🏋️ Train the Model

If you want to train the CNN model again:

```bash
python train.py
```

The trained model can be saved inside:

```text
models/
```

The project also includes Jupyter notebooks for training and experimentation:

```text
CNN_MNIST_Training.ipynb
train.ipynb
```

## 🔮 Future Improvements

* Draw digit directly on a canvas
* Display prediction confidence
* Support multiple handwritten digits
* Improve image preprocessing
* Add prediction history
* Deploy the application online
* Add REST API support
* Add mobile-friendly interface
* Support real-time digit recognition

## 📌 Applications

This project demonstrates the practical use of deep learning and computer vision for:

* Handwritten digit recognition
* Optical Character Recognition (OCR)
* Educational AI applications
* Computer vision projects
* Neural network classification

## 👨‍💻 Author

**Manoj TK**

GitHub:

[https://github.com/manojtk900](https://github.com/manojtk900)

## 📄 License

This project is intended for educational and academic purposes.

````

### Then save it and push it

In your VS Code terminal:

```powershell
git add README.md
git commit -m "Add project README"
git push
````

If you **already created a README directly on GitHub**, don't blindly push this version. In that case, tell me and I'll give you the exact commands to merge the GitHub README with your local project safely.

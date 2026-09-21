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

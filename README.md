# 👨‍💻 Men & Women Image Classification

An image classification project built with **Python, TensorFlow, Keras, and MobileNetV2**. The model uses Transfer Learning and Fine-Tuning to classify images into two categories: Men and Women.

## 🎯 Project Overview

This project uses Deep Learning and Convolutional Neural Networks (CNN) to classify images into two classes:

- Men
- Women

The model is based on the MobileNetV2 architecture and uses data augmentation, dropout, regularization, and fine-tuning to improve classification performance.

## 🧠 Model Architecture

**Base Model:** MobileNetV2

**Framework:** TensorFlow / Keras

**Approach:** Transfer Learning + Fine-Tuning

**Input Image Size:** 224 × 224 × 3

**Output Classes:** 2

### Architecture

1. Image Input (224 × 224 × 3)
2. Data Augmentation
3. Image Rescaling
4. MobileNetV2 Feature Extraction
5. Global Average Pooling
6. Dropout (0.5)
7. Dense Layer (128 neurons, ReLU)
8. Dropout (0.4)
9. Output Layer (2 neurons, Softmax)

## 📂 Dataset

The dataset contains 2,000 images divided into two categories.

| Category | Images |
|---|---:|
| Men | 727 |
| Women | 1,273 |
| **Total** | **2,000** |

### Dataset Split

| Dataset | Images |
|---|---:|
| Training | 1,600 |
| Testing / Validation | 400 |

Images are resized to 224 × 224 pixels and normalized before training.

## 🔄 Data Augmentation

The following augmentation techniques are used:

- Random Horizontal Flip
- Random Rotation
- Random Zoom
- Random Contrast

These techniques help improve generalization and reduce overfitting.

## ⚙️ Training Process

The model is trained in two stages.

### Stage 1: Transfer Learning

- MobileNetV2 pretrained weights are loaded.
- The base model is frozen.
- The classification head is trained.
- Adam optimizer is used.
- Learning Rate: `0.0001`
- Maximum Epochs: 30

### Stage 2: Fine-Tuning

- The last 30 MobileNetV2 layers are unfrozen.
- Batch Normalization layers remain frozen.
- Learning Rate: `0.00001`
- Maximum Epochs: 15

### Training Callbacks

- EarlyStopping
- ReduceLROnPlateau

## 📊 Model Performance

The model achieved **95% accuracy** on the 400-image evaluation split.

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Men | 0.93 | 0.94 | 0.94 |
| Women | 0.97 | 0.96 | 0.96 |
| **Overall Accuracy** | | | **0.95** |

### Confusion Matrix

```text
[[137   8]
 [ 11 244]]
```

- 137 Men images correctly classified.
- 8 Men images incorrectly classified.
- 11 Women images incorrectly classified.
- 244 Women images correctly classified.

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- NumPy
- OpenCV
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## 📁 Project Structure

```text
Men-Women-Image-Classification/
│
├── ProectbyDavoHoso/
│   ├── men/
│   └── women/
│
├── mobilenet_v2_weights.h5
├── men_women_classifier.keras
├── men_women_model.pkl
├── Untitled(2).ipynb
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Men-Women-Image-Classification.git

cd Men-Women-Image-Classification
```

Install dependencies:

```bash
pip install tensorflow numpy pandas opencv-python matplotlib seaborn scikit-learn
```

## ▶️ Model Prediction

Load the trained model:

```python
import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("men_women_classifier.keras")

image = cv2.imread("test_image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224, 224))

image = image.astype("float32") / 255.0
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)

classes = ["Men", "Women"]

print("Prediction:", classes[np.argmax(prediction)])
```

## 💾 Saved Models

The trained model is saved in two formats:

- `men_women_classifier.keras`
- `men_women_model.pkl`

## 👨‍💻 Author

**Davit Poghosyan**

GitHub: [@DavitPoghosyan2007](https://github.com/DavitPoghosyan2007)

---

⭐ If you find this project interesting, consider giving it a star!# Men_Woomen

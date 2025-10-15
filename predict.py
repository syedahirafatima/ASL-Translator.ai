"""
Contains functions: pre_process() and which() that are needed by translator.py for predicting image from webcam
"""
import cv2
import numpy as np
from variables import *
from keras.models import load_model

# Load pretrained CNN Model from MODEL_PATH
model = load_model(MODEL_PATH)

# Automatically detect expected input size from model
INPUT_SHAPE = model.input_shape  # e.g. (None, 64, 64, 3)
IMAGE_SIZE = INPUT_SHAPE[1]      # 64 in this example
CHANNELS = INPUT_SHAPE[3]        # 1 or 3

def pre_process(img_array):
    """
    Pre-processes an image before prediction.
    Automatically adjusts to the model's input shape (grayscale or RGB).
    """
    if CHANNELS == 1:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    else:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    img_array = cv2.resize(img_array, (IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_array.astype("float32") / 255.0

    # If grayscale, add channel dimension
    if CHANNELS == 1:
        img_array = np.expand_dims(img_array, axis=-1)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def which(img_array):
    """
    Takes webcam frame (ROI), preprocesses, and predicts the ASL alphabet.
    Returns: (confidence %, predicted letter)
    """
    img_array = pre_process(img_array)
    preds = model.predict(img_array)
    preds *= 100
    most_likely_class_index = int(np.argmax(preds))
    return preds.max(), LABELS[most_likely_class_index]

import numpy as np
import os, sys
import tensorflow as tf
import cv2
import pathlib
import argparse

# DECLARATIONS
IMG_WIDTH = IMG_HEIGHT = 128
PATH_TO_MODEL = "models/20200221-060223.h5"
font = cv2.FONT_HERSHEY_TRIPLEX

# Load classes into array
class_path = pathlib.Path("hirise-map-proj-v3/testing/")
CLASS_NAMES = [item.name for item in class_path.glob("*")]

# Function to convert image to numpy array
def load_image_into_numpy_array(image):
    return np.array(image).reshape((1, IMG_WIDTH, IMG_HEIGHT, 1)).astype(np.float32)


# Function to return prediction class name
def prediction(arr):
    if arr[0] == 1:
        return CLASS_NAMES[0]
    elif arr[1] == 1:
        return CLASS_NAMES[1]
    elif arr[2] == 1:
        return CLASS_NAMES[2]
    elif arr[3] == 1:
        return CLASS_NAMES[3]
    elif arr[4] == 1:
        return CLASS_NAMES[4]
    elif arr[5] == 1:
        return CLASS_NAMES[5]
    elif arr[6] == 1:
        return CLASS_NAMES[6]
    elif arr[7] == 1:
        return CLASS_NAMES[7]


# Load Model
model = tf.keras.models.load_model(PATH_TO_MODEL)

# Start webcam feed
try:
    feed = cv2.VideoCapture(0)
except ExceptionError as e:
    print(e)

# Let's get classifying
while True:
    # Get the image
    ret, img = feed.read()

    # Convert to grayscale to run prediction
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) * (1.0 / 255)
    gray = cv2.resize(gray, (IMG_HEIGHT, IMG_WIDTH))
    gray = np.reshape(gray, (1, IMG_WIDTH, IMG_HEIGHT, 1)).astype(np.float32)

    # Get prediction
    prd = prediction(model.predict(gray, batch_size=1, steps=1, verbose=0).round()[0])

    # Output image and prediction
    cv2.putText(img, prd, (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("JMARS", img)

    # Press q to end
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

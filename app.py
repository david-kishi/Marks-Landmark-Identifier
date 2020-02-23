import numpy as np
import os, sys
import tensorflow as tf
import cv2
import pathlib

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
    temp = arr.round()
    if temp[0] == 1:
        return arr[0], CLASS_NAMES[0]
    elif temp[1] == 1:
        return arr[1], CLASS_NAMES[1]
    elif temp[2] == 1:
        return arr[2], CLASS_NAMES[2]
    elif temp[3] == 1:
        return arr[3], CLASS_NAMES[3]
    elif temp[4] == 1:
        return arr[4], CLASS_NAMES[4]
    elif temp[5] == 1:
        return arr[5], CLASS_NAMES[5]
    elif temp[6] == 1:
        return arr[6], CLASS_NAMES[6]
    elif temp[7] == 1:
        return arr[7], CLASS_NAMES[7]
    else:
        return 0, "NONE"


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
    prd_base = model.predict(gray, batch_size=1, steps=1, verbose=0)
    prob, prd = prediction(prd_base[0])

    # Output image and prediction
    cv2.putText(img, f"{prd}, {prob}", (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("JMARS", img)

    # Press q to end
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

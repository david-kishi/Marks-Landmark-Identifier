from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

#

# CNN Model
model = Sequential(
    [
        Dense(32, input_shape=(784,)),
        Activation("relu"),
        Dense(10),
        Activation("softmax"),
    ]
)

model.add(Dense(5))
model.add(Activation("relu"))

model.summary()

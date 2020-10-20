"""
Test script to learn Tensorflow
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Dataset of images of numbers from Keras
mnist = keras.datasets.mnist

# Splitting into training and testing data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize colors from 0-255 range to 0-1 range
x_train, x_test = x_train/255.0, x_test/255.0

# Defining neural network model
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10),
])

print(model.summary())

# Loss and Optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optim = keras.optimizers.Adam(lr=0.001)
metrics = ["accuracy"]

# Compile model
model.compile(optimizer= optim, loss= loss, metrics= metrics)

# Training
batch_size = 64
epochs = 5

model.fit(x_train, y_train, batch_size= batch_size, epochs= epochs, verbose= 2, shuffle= True)

# Evaluate model
model.evaluate(x_test, y_test, verbose= True)

# Prediction
predictions = model.predict(x_test, batch_size= batch_size)

# Checking the first 5 predictions
predictionsHead = predictions[0:5]
print( np.argmax(predictionsHead, axis= 1) )
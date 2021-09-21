import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt
fashion_mnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()
train_images=train_images/255.0
test_images=test_images/255.0

def create_model():
    model=tf.keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation="relu"),
        keras.layers.Dense(10)
    ])
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[tf.metrics.SparseCategoricalAccuracy()]
    )
    return model
new_model=create_model()
new_model.fit(train_images,train_labels,epochs=30)
new_model.save("model/my_model1.h5")


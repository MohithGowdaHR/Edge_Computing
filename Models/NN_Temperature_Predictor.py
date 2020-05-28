#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:28:08 2020

@author: mohithgowdahr
"""



import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd

dataset = pd.read_csv("dataset_temperature.csv")


x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1:].values


# create a NN with 2 layers of 16 neurons
model = tf.keras.Sequential()
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mse'])
model.fit(x, y, epochs=1000, batch_size=16)

model.predict([x[0:5].tolist()])



model.save('Temperature_predictor_model')

load_model = tf.keras.models.load_model('Temperature_predictor_model')
converter = tf.lite.TFLiteConverter.from_keras_model(load_model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save the model to disk
open("temperature_predictor.tflite", "wb").write(tflite_model)

#  command xxd -i temperature_predictor.tflite > temperature_predictor.h

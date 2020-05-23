#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:28:08 2020

@author: mohithgowdahr
"""

import csv
import pandas as pd
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix,accuracy_score
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.callbacks import EarlyStopping


dataset = "dataset_temperature.csv"


column_names = ["year", "month", "day", "hour", "minute", "second","recnt_Temperature", 
                "recnt_Humidity",  "Target_Temperature"]             

feature_names = column_names[:-1]
label_name = column_names[-1]

print("Features: {}".format(feature_names))
print("Label: {}".format(label_name))


#

batch_size = 32

train_dataset = tf.data.experimental.make_csv_dataset(
    dataset,
    batch_size,
    column_names=column_names,
    label_name=label_name,
    num_epochs=1)

features, labels = next(iter(train_dataset))

print(features)

def pack_features_vector(features, labels):
  """Pack the features into a single array."""
  features = tf.stack(list(features.values()), axis=1)
  return features, labels

train_dataset = train_dataset.map(pack_features_vector)



features, labels = next(iter(train_dataset))

print(features[:1])
print(labels[:1])


model = tf.keras.Sequential([
  tf.keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(8,)),  # input shape required
  tf.keras.layers.Dense(32, activation=tf.nn.relu),
  tf.keras.layers.Dense(32, activation=tf.nn.relu),
  tf.keras.layers.Dense(8, activation=tf.nn.relu),
  tf.keras.layers.Dense(1)
])
    
optimizer = tf.keras.optimizers.RMSprop(0.001)
model.compile( metrics=['mse'],optimizer=optimizer, loss='mse')#optimizer='adam'
model.fit(features, labels, epochs=30000, batch_size=32)
model.predict(features[:10])
print(labels[:10])
# mse 1.0082    


converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_model = converter.convert()


open("temperature_predictor.tflite", "wb").write(tflite_model)


#  command xxd -i temperature_predictor.tflite > temperature_predictor.h
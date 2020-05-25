#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:28:08 2020

@author: mohithgowdahr
"""



import tensorflow as tf
import numpy as np



dataset = "dataset_temperature.csv"


column_names = ["year", "month", "day", "hour", "minute", "second","recnt_Temperature", 
                "recnt_Humidity",  "Target_Temperature"]             

feature_names = column_names[:-1]
label_name = column_names[-1]

print("Features: {}".format(feature_names))
print("Label: {}".format(label_name))


#

batch_size = 12620

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
model.fit(features, labels, epochs=300, batch_size=1200)

model.fit(np.array(features), labels, epochs=300, batch_size=1200)
model.predict(features[1])
print(labels[:10])
# mse 1.0082    


a = np.array(features).tolist()
b=tf.convert_to_tensor([a], dtype=tf.float32)
model.predict(b)

a =np.array(features[0])
model.predict([[2020. ,    4. ,   27. ,    0. ,   20. ,    0. ,   79. ,   60.4]])




converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()


open("temperature_predictor.tflite", "wb").write(tflite_model)


#  command xxd -i temperature_predictor.tflite > temperature_predictor.h
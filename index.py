#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:26:49 2020

@author: mohithgowdahr
"""


from sklearn.externals import joblib
from datetime import datetime 

year = ""
month = ""
day = ""
hour = ""
minute = ""
second = ""

temperature_model = joblib.load('temperature.pkl')
humidity_model = joblib.load('temperature.pkl')

def predict(Currentdatetime,pastHumidity,pastTemperature):
    
    datetime_object = datetime.strptime(Currentdatetime.replace("-","/"), '%Y/%m/%d %H:%M:%S %Z')
    year = (datetime_object.strftime("%Y"))
    month = (datetime_object.strftime("%m"))
    day = (datetime_object.strftime("%d"))
    hour = (datetime_object.strftime("%H"))
    minute = (datetime_object.strftime("%M"))
    second = (datetime_object.strftime("%S"))
    
    temperature_predition = temperature_model.predict([[year,month,day,hour,minute,second,pastTemperature,pastHumidity]])
    
    humidity_predition = humidity_model.predict([[year,month,day,hour,minute,second,pastHumidity,pastTemperature]])

    print("Temperature","Humidity")
    print(round(temperature_predition[0],1),round(humidity_predition[0]))
    return(round(temperature_predition[0],1),round(humidity_predition[0]))
    
predict("2020-01-05 10:20:40 UTC",34.0,34.5)
# temp 34.5 humid  34
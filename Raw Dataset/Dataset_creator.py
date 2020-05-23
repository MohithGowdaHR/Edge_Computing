#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:34:08 2020

@author: mohithgowdahr
"""

import csv
import pandas as pd
from datetime import datetime


dataset = pd.read_csv("Dataset.csv")

time = []
temperature = []
humidity = []


for i in range(len(dataset)):
    if (not(pd.isna(dataset.iat[i, 6])) and 
        not(pd.isna(dataset.iat[i, 7]))):
        time.append(dataset.iat[i, 0])
        temperature.append(dataset.iat[i, 6])
        humidity.append(dataset.iat[i, 7])
        
        
year = []
month = []
day = []
hour = []
minute = []
second = []

for i in time:
    datetime_object = datetime.strptime(i.replace("-","/"), '%Y/%m/%d %H:%M:%S %Z')
    year.append(datetime_object.strftime("%Y")+".0")
    month.append(datetime_object.strftime("%m")+".0")
    day.append(datetime_object.strftime("%d")+".0")
    hour.append(datetime_object.strftime("%H")+".0")
    minute.append(datetime_object.strftime("%M")+".0")
    second.append(datetime_object.strftime("%S")+".0")
    

with open("dataset_humidity.csv",mode="a+",newline='') as file_obj:
    writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["year","month","day","hour","minute","second","recnt_Humidity","recnt_Temperature","Target_Humidity"])
with open("dataset_temperature.csv",mode="a+",newline='') as file_obj:
    writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["year","month","day","hour","minute","second","recnt_Temperature","recnt_Humidity","Target_Temperature"])
    
for i in range(1,len(year)):
    with open("dataset_humidity.csv",mode="a+",newline='') as file_obj:
        writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([year[i],month[i],day[i],hour[i],minute[i],second[i],humidity[i-1],temperature[i-1],humidity[i]])
    with open("dataset_temperature.csv",mode="a+",newline='') as file_obj:
        writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([year[i],month[i],day[i],hour[i],minute[i],second[i],temperature[i-1],humidity[i-1],temperature[i]])
        

    



            
        
        
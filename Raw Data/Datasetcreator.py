#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:11:10 2020

@author: mohithgowdahr
"""

import pandas as pd


h_data = pd.read_csv("hum.csv")
t_data = pd.read_csv("temp.csv")
time = []
humid = []
temp = []
year = []
month = []
day = []
hour = []
minute = []
second = []

for i in range(len(h_data)):
    time.append(h_data.iloc[i,0])
    humid.append(h_data.iloc[i,2])
    temp.append(t_data.iloc[i,-1])
    
    
from datetime import datetime 

for i in time:
    datetime_object = datetime.strptime(i.replace("-","/"), '%Y/%m/%d %H:%M:%S %Z')
    year.append(datetime_object.strftime("%Y"))
    month.append(datetime_object.strftime("%m"))
    day.append(datetime_object.strftime("%d"))
    hour.append(datetime_object.strftime("%H"))
    minute.append(datetime_object.strftime("%M"))
    second.append(datetime_object.strftime("%S"))
    
import csv
with open("dataset_humidity.csv",mode="a+",newline='') as file_obj:
    writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["index","year","month","day","hour","minute","second","past_Humid","past_Temp","Target_Humid"])
with open("dataset_temperature.csv",mode="a+",newline='') as file_obj:
    writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["index","year","month","day","hour","minute","second","past_Temp","past_Humid","Target_Temperature"])
    
for i in range(len(year)):
    with open("dataset_humidity.csv",mode="a+",newline='') as file_obj:
        writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([i+1,year[i],month[i],day[i],hour[i],minute[i],second[i],humid[i-1],temp[i-1],humid[i]])
    with open("dataset_temperature.csv",mode="a+",newline='') as file_obj:
        writer = csv.writer(file_obj,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([i+1,year[i],month[i],day[i],hour[i],minute[i],second[i],temp[i-1],humid[i-1],temp[i]])
        

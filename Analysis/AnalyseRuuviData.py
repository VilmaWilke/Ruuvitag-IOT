# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:09:51 2021

@author: Vilma
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

dropColumns = ["name", 
               "accelerationAngleFromX", 
               "accelerationAngleFromY", 
               "accelerationAngleFromZ", 
               "accelerationTotal", 
               "accelerationX", 
               "accelerationY", 
               "accelerationZ", 
               "dataFormat"]

#Read data in csv format
RvData = pd.read_csv("Data.csv")

#Remove data not used in this analysis. As the sensors are stationary in this setup, acceleration information will not change
RvData = RvData.drop(dropColumns, axis=1)

#Convert time column in to datetime format
RvData["time"] = pd.to_datetime(RvData["time"], errors='coerce')


#Split data by each of the three sensors
rv1, rv2, rv3 = [x for _, x in RvData.groupby(RvData['mac'])]



#Matplotlib
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(rv1["time"], rv1["humidity"])
ax1.plot(rv2["time"], rv2["humidity"])
ax1.plot(rv3["time"], rv3["humidity"])

ax2.plot(rv1["time"], rv1["temperature"])
ax2.plot(rv2["time"], rv2["temperature"])
ax2.plot(rv3["time"], rv3["temperature"])

ax3.plot(rv1["time"], rv1["pressure"])
ax3.plot(rv2["time"], rv2["pressure"])
ax3.plot(rv3["time"], rv3["pressure"])

ax4.plot(rv1["time"], rv1["dewPoint"])
ax4.plot(rv2["time"], rv2["dewPoint"])
ax4.plot(rv3["time"], rv3["dewPoint"])

#Format plot
xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')

plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)


ax1.set_title("Humidity")
ax2.set_title("Temperature")
ax3.set_title("Pressure")
ax4.set_title("DewPoint")

ax1.xaxis.set_major_formatter(xfmt)
ax2.xaxis.set_major_formatter(xfmt)
ax3.xaxis.set_major_formatter(xfmt)
ax4.xaxis.set_major_formatter(xfmt)

plt.tight_layout()

plt.show()
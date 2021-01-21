# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:20:55 2021

@author: Vilma
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from RuuviAnalysis.ImportRV import read__rv_input_data
from RuuviAnalysis.PredictRV import *

inputFile = "Data.csv"
dropColumns = ["name", 
               "accelerationAngleFromX", 
               "accelerationAngleFromY", 
               "accelerationAngleFromZ", 
               "accelerationTotal", 
               "accelerationX", 
               "accelerationY", 
               "accelerationZ", 
               "dataFormat"]


#Call function from library to prepare the data
rv1, rv2, rv3 = read__rv_input_data(inputFile, dropColumns)

#Get the average, maximum, and minimum values for one of the sensors
rv1_avg = get_daily_average(rv1)
rv1_min = get_daily_min(rv1)
rv1_max = get_daily_max(rv1)



#Matplotlib
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(rv1_avg["humidity"], label="Average")
ax1.plot(rv1_min["humidity"], label="Min")
ax1.plot(rv1_max["humidity"], label="Max")

ax2.plot(rv1_avg["temperature"], label="Average")
ax2.plot(rv1_min["temperature"], label="Min")
ax2.plot(rv1_max["temperature"], label="Max")

ax3.plot(rv1_avg["pressure"], label="Average")
ax3.plot(rv1_min["pressure"], label="Min")
ax3.plot(rv1_max["pressure"], label="Max")

ax4.plot(rv1_avg["dewPoint"], label="Average")
ax4.plot(rv1_min["dewPoint"], label="Min")
ax4.plot(rv1_max["dewPoint"], label="Max")

#Format plot

plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)

ax1.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax2.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax3.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax4.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))

ax1.tick_params(labelsize=7)
ax2.tick_params(labelsize=7)
ax3.tick_params(labelsize=7)
ax4.tick_params(labelsize=7)

ax1.set_title("Humidity")
ax2.set_title("Temperature")
ax3.set_title("Pressure")
ax4.set_title("DewPoint")

ax1.set(xlabel="Time(H)", ylabel="Humidity (%)")
ax2.set(xlabel="Time(H)", ylabel="Temperature (C)")
ax3.set(xlabel="Time(H)", ylabel="Pressure (Pa)")
ax4.set(xlabel="Time(H)", ylabel="Dew point (C)")

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

plt.tight_layout()

plt.show()

fig.set_size_inches(18.5, 10.5)
fig.savefig('Plots/AverageDataDemo.png', dpi=100)

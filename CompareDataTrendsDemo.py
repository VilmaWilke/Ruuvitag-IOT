# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:41:38 2021

@author: Vilma
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from RuuviAnalysis.ImportRV import read__rv_input_data

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

#Matplotlib
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

#Compare data on two different axes, but display the lines in the same legend
ax12 = ax1.twinx()
a, = ax1.plot(rv1["humidity"], color='blue', label="Humidity")
b, = ax12.plot(rv1["pressure"], color='orange', label="Pressure")
p = [a, b]
ax1.legend(p, [p_.get_label() for p_ in p],
           loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))

ax22 = ax2.twinx()
a, = ax2.plot(rv1["temperature"], color='green', label="Temperature")
b, = ax22.plot(rv1["dewPoint"], color='red', label="Dew Point")
p = [a, b]
ax2.legend(p, [p_.get_label() for p_ in p],
           loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))

ax32 = ax3.twinx()
a, = ax3.plot(rv1["airDensity"], color='cyan', label="Air Density")
b, = ax32.plot(rv1["absoluteHumidity"], color='purple', label="Absolute Humidity")
p = [a, b]
ax3.legend(p, [p_.get_label() for p_ in p],
           loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))


#Format plot
xfmt = mdates.DateFormatter('%d-%m %H:%M')

plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

ax1.tick_params(labelsize=7)
ax2.tick_params(labelsize=7)
ax3.tick_params(labelsize=7)

ax1.set_title("Humidity and Pressure")
ax2.set_title("Temperature and Dew Point")
ax3.set_title("Air Density and Absolute Humidity")

ax1.xaxis.set_major_formatter(xfmt)
ax2.xaxis.set_major_formatter(xfmt)
ax3.xaxis.set_major_formatter(xfmt)

ax1.grid()
ax2.grid()
ax3.grid()

ax1.set(xlabel="Time(M/D/H:m)", ylabel="Humidity (%)")
ax2.set(xlabel="Time(M/D/H:m)", ylabel="Temperature (C)")
ax3.set(xlabel="Time(M/D/H:m)", ylabel="Pressure (Pa)")

fig.subplots_adjust(hspace=.5)

plt.show()

fig.set_size_inches(18.5, 10.5)
fig.savefig('Plots/CompareDataTrendDemo.png', dpi=100)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:09:51 2021

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
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(rv1["humidity"], label="Sensor 1")
ax1.plot(rv2["humidity"], label="Sensor 2")
ax1.plot(rv3["humidity"], label="Sensor 3")

ax2.plot(rv1["temperature"], label="Sensor 1")
ax2.plot(rv2["temperature"], label="Sensor 2")
ax2.plot(rv3["temperature"], label="Sensor 3")

ax3.plot(rv1["pressure"], label="Sensor 1")
ax3.plot(rv2["pressure"], label="Sensor 2")
ax3.plot(rv3["pressure"], label="Sensor 3")

ax4.plot(rv1["dewPoint"], label="Sensor 1")
ax4.plot(rv2["dewPoint"], label="Sensor 2")
ax4.plot(rv3["dewPoint"], label="Sensor 3")

#Format plot
xfmt = mdates.DateFormatter('%d-%m %H:%M')

ax1.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax2.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax3.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax4.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))

plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)

ax1.tick_params(labelsize=7)
ax2.tick_params(labelsize=7)
ax3.tick_params(labelsize=7)
ax4.tick_params(labelsize=7)

ax1.set_title("Humidity")
ax2.set_title("Temperature")
ax3.set_title("Pressure")
ax4.set_title("DewPoint")

ax1.set(xlabel="Time(M/D/H:m)", ylabel="Humidity (%)")
ax2.set(xlabel="Time(M/D/H:m)", ylabel="Temperature (C)")
ax3.set(xlabel="Time(M/D/H:m)", ylabel="Pressure (Pa)")
ax4.set(xlabel="Time(M/D/H:m)", ylabel="Dew point (C)")

ax1.xaxis.set_major_formatter(xfmt)
ax2.xaxis.set_major_formatter(xfmt)
ax3.xaxis.set_major_formatter(xfmt)
ax4.xaxis.set_major_formatter(xfmt)

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

plt.tight_layout()

plt.show()

fig.set_size_inches(18.5, 10.5)
fig.savefig('Plots/ReadDataDemo.png', dpi=100)
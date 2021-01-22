# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:20:55 2021

@author: Vilma
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
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

#Set data yo analyse
X = rv1.index.to_frame()
y =  rv1['temperature']

#Get a segment to train the data on
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05)

#Set up regression with decision tree.
regressor = DecisionTreeRegressor(max_depth=20)
regressor.fit(X_train.values.reshape(-1,1), y_train.values.reshape(-1,1))

#Get predictions
y_pred = regressor.predict(X_test.values.reshape(-1,1))


#Plot to compare
fig, (ax1)= plt.subplots(1,1)

ax1.scatter(X_test, y_pred, label="Predicted", marker=",")
ax1.scatter(X_test, y_test, label="Real", marker=".")


#Format plot
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
ax1.legend(loc= 'upper left', fontsize= 'small', bbox_to_anchor=(1.1, 1))
ax1.tick_params(labelsize=7)
ax1.set_title("Decision tree linear regression")
ax1.set(xlabel="Time(H)", ylabel="Temperature (C)")
ax1.grid()
plt.tight_layout()
plt.show()

fig.set_size_inches(18.5, 10.5)
fig.savefig('Plots/LinearRegressionDataDemo.png', dpi=100)




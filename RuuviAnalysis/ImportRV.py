# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:09:51 2021

@author: Vilma
"""

import pandas as pd
import numpy as np
import datetime


def read__rv_input_data(inputFile, dropColumns):
    """Returns prepared data from csv format"""  
    
    #Read data in csv format
    RvData = pd.read_csv(inputFile)
    
    #Remove data not used in this analysis. As the sensors are stationary in this setup, acceleration information will not change
    RvData = RvData.drop(dropColumns, axis=1)
    
    #Convert time column in to datetime format
    RvData["time"] = pd.to_datetime(RvData["time"], errors='raise')
    
    #Set datetime as index
    RvData.set_index("time", inplace=True)
    
    #Split data by each of the sensors, then return
    return ([x for _, x in RvData.groupby(RvData['mac'])])


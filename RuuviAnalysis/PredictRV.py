# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:07:15 2021

@author: Vilma
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_daily_average(rv):
    """Returns the average hourly values of all existing columns"""
    
    #Make sure new dataframe is empty
    df = pd.DataFrame()   
    
    for x in range(0, 24):
        tmp = rv.loc[rv.index.strftime("%H") == "{0:0=2d}".format(x)].mean(axis=0)
        df = df.append(tmp, ignore_index=True)
        
    return df

def get_daily_min(rv):
    """Returns the minimum hourly values of all existing columns"""
    #Make sure new dataframe is empty
    df = pd.DataFrame()   
    
    for x in range(0, 24):
        tmp = rv.loc[rv.index.strftime("%H") == "{0:0=2d}".format(x)].min(axis=0)
        df = df.append(tmp, ignore_index=True)
        
    return df

def get_daily_max(rv):
    """Returns the maximum hourly values of all existing columns"""
    
    #Make sure new dataframe is empty
    df = pd.DataFrame()   
    
    for x in range(0, 24):
        tmp = rv.loc[rv.index.strftime("%H") == "{0:0=2d}".format(x)].max(axis=0)
        df = df.append(tmp, ignore_index=True)
        
    return df

def get_hour_data(rv, hour):
    """Returns all data that occurs at a given hour"""
    
    #Make sure new dataframe is empty
    df = pd.DataFrame()   
    
    tmp = rv.loc[rv.index.strftime("%H") == "{0:0=2d}".format(hour)]
    df = df.append(tmp)
        
    return df

def get_day_data(rv, day):
    """Returns all data that occurs at a given day"""
    
    #Make sure new dataframe is empty
    df = pd.DataFrame()   
    
    tmp = rv.loc[rv.index.strftime("%d") == "{0:0=2d}".format(day)]
    df = df.append(tmp)
        
    return df
    
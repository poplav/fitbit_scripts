#!/usr/bin/python

import MySQLdb
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readCsv(file):
    #Read in csv
    df = pd.read_csv(file)
    #Convert Strings to Dates
    df['Date'] = pd.to_datetime(pd.Series(df['Date']))
    return df

def getAvgValLookBack(lookBack, value):
    startDate = datetime.datetime.now() + datetime.timedelta(-lookBack)
    tempDf = df[(df["Date"] > startDate)]
    print tempDf
    return tempDf[value].sum() / tempDf[value].count()

def getAvgValOnDay(day, value):
    tempDf = df[(df["weekday"] == day)]
    print tempDf
    return tempDf[value].sum() / tempDf[value].count()

def getValDayDistribution(value):
    vals = []
    for i in xrange(0,6):
        vals.append(getAvgValOnDay(i, "Minutes Asleep"))
    return vals;

df = readCsv('/home/mike/Desktop/fitbit_export_20150421.csv')
df["weekday"] = df["Date"].apply(lambda x: x.weekday())
#print df
print getAvgValLookBack(17, "Minutes Asleep")
print getAvgValOnDay(1, "Minutes Asleep")
print getValDayDistribution("Minutes Asleep")
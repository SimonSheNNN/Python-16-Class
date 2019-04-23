#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 02:33:35 2019

@author: Simon
"""

import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_csv('echo.csv') #read data
basebp = d['basebp']    #base blood pressure
legend = ['basebp', 'sbp']
sbp = d['sbp']      #systolic blood pressure
plt.hist([basebp, sbp], color=['blue', 'green'])    
plt.xlabel("Blood Pressure")
plt.ylabel("Frequency")
plt.legend(legend)
plt.title('Blood Pressure of Patients for a Drug Test')
plt.show()
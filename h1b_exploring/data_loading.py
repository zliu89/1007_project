'''
Created on Dec 1, 2016

@author: Yovela
'''

import sys
import pandas as pd
import numpy as np
from class_collections_ranking import *

def h1bdata_loading():
    """
    used at the start of main function. safely input the data set from the external csv file.
    Raise exception when input failed

    return
    ======
    a verified DataFrame

    """
    print ("Welcome to Our H1b Analysis System! \n")
    print ("loading data.......... \n")
    data = {}
    for year in range(2010,2017):
        data[year]= pd.read_csv('DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
    print("dataset loaded successfully >>>")
    print(">>>")
    return data

 

'''
data = {}
for year in range(2010,2017):
    data[year]= pd.read_csv('/Users/Yovela/Desktop/1007_project/1007_project//H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
    
merged_data = pd.concat([data[year] for year in range(2010,2017)], ignore_index= True)

state_data = state_level(merged_data)
city_data = city_level(merged_data)
industry_data = industry_level(merged_data)
company_data = company_level(merged_data)
'''
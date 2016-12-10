"""
Loading the dataset but also checking the loaded dataset

Author: Sheng Liu (sl5924)

"""
import pandas as pd
import sys
from exception_list import *

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
    print ("dataset loaded successfully >>>")
    print (">>>"),
    return data



def option_input():

    key = input("Please select one: ")
    options = list('abcr')
    
    if key == 'quit':
        print ("You have quited the system.")
        sys.exit()
    
    if not(key in options):
        raise wrong_option_exception
    return key

def get_input(path):
    """
    given a file path, verify the input dataset
    argument
    ========
    path: string showing the path of .csv file

    return
    ======
    checked dataframe
    """

    df = pd.read_csv(path)
    attributes = [u'YEAR', u'CASE_NUMBER', u'STATUS', u'VISA_CLASS', u'EMPLOYER_NAME', u'EMPLOYER_CITY',
             u'EMPLOYER_STATE', u'SOC_CODE', u'SOC_NAME', u'JOB_TITLE', u'PREVAILING_WAGE',
             u'FULL_TIME']

    for col in df.columns:
        if not(col in attributes):
            raise wrong_dataset_exception
    return df
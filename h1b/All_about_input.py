"""
Loading the dataset but also checking the loaded dataset

Author: Sheng Liu (sl5924)

"""
import pandas as pd
import sys
from exception_list import *

def safely_input():
    """
    used at the start of main function. safely input the data set from the external csv file.
    Raise exception when input failed

    return
    ======
    a verified DataFrame

    """
    print "Welcome to Our H1b Analysis System! \n"
    path = "2016_Data.csv"
    while Ture:
        try:
            raw_data = get_input(path)
            break
        except IOError:
            path = raw_input( "Can not locate the dataset file, type in a valid path or type 'quit' to exit \n")
        except Wrong_dataset_exception:
            path = raw_input( "Load a wrong dataset, please type in a valid path or type 'quit' to exit \n")
        if path == 'quit':
            sys.exit()
    return raw_data


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

    data = pd.read_csv(path)
    attributes = [u'YEAR', u'CASE_NUMBER', u'STATUS', u'VISA_CLASS', u'EMPLOYER_NAME', u'EMPLOYER_CITY',
             u'EMPLOYER_STATE', u'SOC_CODE', u'SOC_NAME', u'JOB_TITLE', u'PREVAILING_WAGE',
             u'FULL_TIME']

    for col in df.columns:
        if not(col in attributes):
            raise Wrong_dataset_exception
    return df
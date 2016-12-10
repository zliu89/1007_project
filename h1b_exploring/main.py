"""
This is the main module of the project, all the functions are imported from package H1b

Author:  ShengLiu (sl5924)
"""

from H1b import *

import sys
import pandas as pd
from exception_list import wrong_option_exception

from All_about_input import option_input
from h1b_data import h1b_data
from Overview import overview
from Location import location
from company import company_exploring
from industry import industry_exploring


def main():
    """
    The whole project start here.
    """

    # start at loading the dataset
    data = {}
    for year in range(2010,2017):
        data[year]= pd.read_csv('/DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
    merged_data = pd.concat([h1b_data[year] for year in range(2010,2017)], ignore_index= True)
    raw_data = h1b_data(data)
    
    print("dataset loaded successfully >>>")
    print(">>>")

    # Then clean the data
    h1b_data = Clean_df(raw_data)
    print("data cleaned >>>")


    while True:
        try:
            print ("================================ H1b Visa Approve Rate Exploring ================================")
            print ("")
            print ("                             How do you want to explore the H1b Data?                            ")
            print ("                              <a>  : Overview                              		                 ")
            print ("                              <b>  : Location                                                    ")
            print ("                              <c>  : Industry                                                    ")
            print ("                              <d>  : Company                                                     ")  
            print ("")
            print ("=================================================================================================")

            key = option_input()
            if key == 'a':
                overview(h1b_data)
            if key == 'b':
                location(h1b_data)
            if key == 'c':
                industry_exploring(merged_data)
            if key == 'd':
                company_exploring(merged_data)
        except wrong_option_exception:
            print ("Invalid option, please reselect.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit()


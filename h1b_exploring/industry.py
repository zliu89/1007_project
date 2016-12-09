

import sys
import pandas as pd

from All_about_input import option_input
from exception_list import wrong_option_exception

from class_collections_ranking import industry_level
from popular_industry import popular_industry
from customized_industry import customized_industry

'''
industry_exploring(merged_data)
'''
def industry_exploring(data):
    
    
    industry_data = industry_level(data)
    
    Flag = True
    
    while Flag:
        try:
    

            print ("================================ H1b Visa Approve Rate Exploring ================================")
            print ("")
            print ("                             Please choose ONE level you interested in                           ")
            print ("                              <a>  : Popular Industry                                            ")
            print ("                              <b>  : Customized Job Inquiry                                      ")
            print ("                              <r>  : Go back to main menu                                        ")  
            print ("")
            print ("=================================================================================================")
   
            key = option_input()
            if key == 'a':
                popular_industry(industry_data)
            if key == 'b':
                customized_industry(industry_data, data)
            if key == 'r':
                Flag = False
        except wrong_option_exception:
            print ("Invalid option, please reselect.")
            
            
            
if __name__ == '__main__':
    data = {}
    for year in range(2010,2017):
        data[year]= pd.read_csv('/Users/yuweitu/Documents/Programming/DSGA1007_Project/DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
    merged_data = pd.concat([data[year] for year in range(2010,2017)], ignore_index= True)
    industry_exploring(merged_data)
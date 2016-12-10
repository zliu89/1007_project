'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
import pandas as pd

from h1b_exploring.All_about_input import option_input
from h1b_exploring.exception_list import wrong_option_exception

from h1b_exploring.class_collections_ranking import company_level
from h1b_exploring.popular_company import popular_company
from h1b_exploring.customized_company import customized_company


# company_exploring(merged_data)

def company_exploring(data):
    
    company_data = company_level(data)
    
    Flag = True
    while Flag:
        try:
            

            print ("================================ H1b Visa Approve Rate Exploring ================================")
            print ("")
            print ("                             Please choose ONE level you interested in                           ")
            print ("                              <a>  : Popular Company                                             ")
            print ("                              <b>  : Customized Company Inquiry                                  ")
            print ("                              <r>  : Go back to the main menu                                    ")  
            print ("")
            print ("=================================================================================================")
    


            key = option_input()
            if key == 'a':
                popular_company(company_data)
            if key == 'b':
                customized_company(company_data)
            if key == 'r':
                Flag = False
        
        except wrong_option_exception:
            print ("Invalid option, please reselect.")
            
            
            
if __name__ == '__main__':
    data = {}
    for year in range(2010,2017):
        data[year]= pd.read_csv('/Users/yuweitu/Documents/Programming/DSGA1007_Project/DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
    merged_data = pd.concat([data[year] for year in range(2010,2017)], ignore_index= True)
    company_exploring(merged_data)
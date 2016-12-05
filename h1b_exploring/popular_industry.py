'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
from class_collections_ranking import *

'''
popular_industry(industry_data)
'''

def popular_industry (df):
    

    print ("================================ H1b Visa Approve Rate Exploring ================================")
    print ("")
    print ("                             Please choose ONE topic you interested in                           ")
    print ("                              <a>  : Application Pull                                            ")
    print ("                              <b>  : Approve Rate                                                ")
    print ("                              <c>  : Average Wage                                                ")
    print ("                              <r>  : Go back to previous directory                               ")  
    print ("")
    print ("=================================================================================================")
    Flag = True
    while Flag:
        try:
            key = option_input()
            if key == 'a':
                industry_level.occupation_rank(df, 10, "application_pool")
            if key == 'b':
                industry_level.occupation_rank(df, 10, "approval_rate")
            if key == 'c':
                industry_level.occupation_rank(df, 10, "average_wage")
            if key == 'r':
                Flag = False
        except wrong_option_exception:
            print ("Invalid option, please reselect.")
'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
from all_about_input import *
from class_collections_ranking import *
from popular_company import *
from customized_company import *



# company_exploring(merged_data)

def company_exploring(data):
    
    company_data = company_level(data)


    print ("================================ H1b Visa Approve Rate Exploring ================================")
    print ("")
    print ("                             Please choose ONE level you interested in                           ")
    print ("                              <a>  : Popular Industry                                            ")
    print ("                              <b>  : Customized Job Inquiry                                      ")
    print ("                              <r>  : Go back to ALL_about_Input menu                                        ")  
    print ("")
    print ("=================================================================================================")
    Flag = True
    while Flag:
        try:
            key = option_input()
            if key == 'a':
                popular_company(data)
            if key == 'b':
                customized_company(data)
            if key == 'r':
                Flag = False
        
        except wrong_option_exception:
            print ("Invalid option, please reselect.")
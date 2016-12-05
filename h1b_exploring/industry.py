


import sys
from class_collections_ranking import *
from popular_industry import *
from customized_industry import *

'''
industry_exploring(merged_data)
'''
def industry_exploring(data):
    
    industry_data = industry_level(data)

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
                popular_industry(industry_data)
            if key == 'b':
                customized_industry(industry_data)
            if key == 'r':
                Flag = False
        except wrong_option_exception:
            print ("Invalid option, please reselect.")

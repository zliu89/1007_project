'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt
from class_collections_ranking import *


def customized_company(company_data):
    
    company_name_list = company_data.newdf.index
    
    while True:
        try:
            print ("================================ H1b Visa Approve Rate Exploring ================================")
            print ("")
            user_input = input ("                      Please Input Your Interested Company Name                          ")
            print ("")
            print ("=================================================================================================")
            user_input = user_input.upper()
            user_company_list = identify_company_name(user_input)
            user_answer = input("if there are companies you interested in, please enter yes; otherwise, enter no")
            
            if user_answer == 'yes':
                search_company(company_data, user_company_list)
            else:
                raise Invalid_Company_Name
            
        except Invalid_Company_Name:
            print ("Invalid company name, please input again")

   
    
    
    def identify_company_name(user_company):
    # generate a list contains all matching company names
        user_company_list = []
        for i in range(len(company_name_list)):
            if user_company in company_name_list[i]:
                user_company_list.append(company_name_list[i])
                
        if len(user_company_list)<=10 and len(user_company_list) >0:
            for user_company in user_company_list:
                print(user_company)
        elif len(user_company_list)>10:
            print("can't accurately locate your interested company, please try to enter the full name")
        elif len(user_company_list) == 0:
            print("can't find your interested company, please re-enter a name")
        
        return user_company_list
    
    
    def search_company(company_data, company_name_list):
    
        df = company_data.newdf.ix[company_name_list]
        print(df.to_string())
        print("The total number of application pool is", df["application_pool"].sum())
        print("The total number of approved case is", df["approved_case"].sum())
        print("The approval rate is", df["approved_case"].sum()/df["application_pool"].sum())
        print("The average wage for this company is",df["average_wage"].sum()/len(df))  
        return
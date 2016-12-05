'''
Created on Nov 27, 2016

@author: Yovela
'''

import sys
from all_about_input import *
from class_collections_ranking import *

'''
industry_data = industry_level(merged_data)
customized_industry(industry_data)

'''
data = {}
for year in range(2010,2013):
    data[year]= pd.read_csv('DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
merged_data = pd.concat([data[year] for year in range(2010,2013)], ignore_index= True)

def customized_industry(df):
    
    industry_list = df.newdf.index
    
    while True:
        try:
            print ("================================ H1b Visa Approve Rate Exploring ================================")
            print ("")
            user_input = input ( "Please Input Your Interested Industry Name, i.e: computer, business, engineering"   )
            print ("=================================================================================================")
            industry_name = identify_industry(user_input)
            search_industry(industry_name)
# TODO: print the whole industry list           
        except Invalid_Industry_Name:
            print ("Invalid industry name, please input again")

    def search_industry(industry_name):
        job_titles = merged_data[merged_data['descrpt'] == industry_name]['SOC_NAME'].drop_duplicates()
        print("The total application pool for " + industry_name + " is: \n")
        print(industry_level.industry_application_pool(df, industry_name))
        print("The total number of approved case for " + industry_name + " is: \n")
        print(industry_level.industry_approved_case(df, industry_name))
        print("The average approval rate for " + industry_name + " is: \n")
        print(industry_level.industry_approval_rate(df, industry_name))
        print("The average wage for " + industry_name + " is: \n")
        print(industry_level.industry_average_wage(df, industry_name))
        print("All related job titles are listed below:")
        print(job_titles.values)
        
        return
        
        
    def identify_industry(user_input):
        
        industry_keyword = user_input.capitalize()
        user_industry_list = []
        for i in range(len(industry_list)):
            if industry_keyword in industry_list[i]:
                user_industry_list.append(industry_list[i])
                print(i,industry_list[i])
           
        if len(user_industry_list) == 1:
            user_input = print("is it the industry you interested in? please enter yes or no")
            if user_input == "yes":
                user_industry = user_industry_list[0]
            else:
                raise Invalid_Industry_Name
            
        if len(user_industry_list) > 1:
            user_choice = print("please choose an industry you interested in, enter the number before it")
            if int(user_choice) >= 0 and int(user_choice)<= len(user_industry_list):
                user_industry = user_industry_list[int(user_choice)]
            else:
                raise Invalid_Industry_Name
            
        if len(user_industry_list) == 0:
            raise Invalid_Industry_Name
            
        return user_industry
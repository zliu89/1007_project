'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt

class state_level:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.newdf = state_level.state(self, dataset)

    def state(self, dataset):
    # calculate required statistics
        application_pool = (dataset.groupby("EMPLOYER_STATE").count())["STATUS_APPROVE"]
        approved_case = (dataset.groupby("EMPLOYER_STATE").sum())["STATUS_APPROVE"]
        approval_rate = (dataset.groupby("EMPLOYER_STATE").mean())["STATUS_APPROVE"]
        average_wage = (dataset.groupby("EMPLOYER_STATE").mean())["PREVAILING_WAGE"]
    
    # create a new DataFrame and rename indexes
        state_data = pd.concat([application_pool, approved_case, approval_rate,average_wage], axis =1)
        state_data.columns.values[0] = "application_pool"
        state_data.columns.values[1] = "approved_case"
        state_data.columns.values[2] = "approval_rate"
        state_data.columns.values[3] = "average_wage"
    
        return state_data

    def state_application_pool(self, state_level, state):
        return state_level.newdf.ix[state, "application_pool"]
    
    def state_approved_case(self, state_level, state):
        return state_level.newdf.ix[state, "approved_case"]
    
    def state_approval_rate(self, state_level, state):
        return state_level.newdf.ix[state, "approval_rate"]
    
    def state_average_wage(self, state_level, state):
        return state_level.newdf.ix[state, "average_wage"]
        
    # TODO: inputing a state, return related company and occupation rank
    
    
class city_level:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.newdf = city_level.city(self,dataset)

    def city(self,dataset):
    # calculate required statistics
        application_pool = (dataset.groupby("EMPLOYER_CITY").count())["STATUS_APPROVE"]
        approved_case = (dataset.groupby("EMPLOYER_CITY").sum())["STATUS_APPROVE"]
        approval_rate = (dataset.groupby("EMPLOYER_CITY").mean())["STATUS_APPROVE"]
        average_wage = (dataset.groupby("EMPLOYER_CITY").mean())["PREVAILING_WAGE"]
    
    # create a new DataFrame and rename indexes
        city_data = pd.concat([application_pool, approved_case, approval_rate,average_wage], axis =1)
        city_data.columns.values[0] = "application_pool"
        city_data.columns.values[1] = "approved_case"
        city_data.columns.values[2] = "approval_rate"
        city_data.columns.values[3] = "average_wage"
    
        return city_data

    def city_application_pool(self, city_level, city):
        return city_level.newdf.ix[city, "application_pool"]

    def city_approved_case(self, city_level, city):
        return city_level.newdf.ix[city, "approved_case"]
    
    def city_approval_rate(self, city_level, city):
        return city_level.newdf.ix[city, "approval_rate"]
    
    def city_average_wage(self, city_level, city):
        return city_level.newdf.ix[city, "average_wage"]
    
    def city_rank(self, city_level, n, indicator):
        city_rank = city_level.newdf.sort_values(by = indicator).ix[-n:, indicator]
        city_rank.plot(kind = "barh", alpha = 0.7)
        plt.title("Top"+ str(n) + " Cities with highest " + indicator)
        return     

'''
industry level
TODO: Group occupations
'''

class industry_level:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.newdf = industry_level.industry(self, dataset)

    def industry(self, dataset):
    # calculate required statistics
        application_pool = (dataset.groupby("SOC_NAME").count())["STATUS_APPROVE"]
        approved_case = (dataset.groupby("SOC_NAME").sum())["STATUS_APPROVE"]
        approval_rate = (dataset.groupby("SOC_NAME").mean())["STATUS_APPROVE"]
        average_wage = (dataset.groupby("SOC_NAME").mean())["PREVAILING_WAGE"]
    
    # create a new DataFrame and rename indexes
        industry_data = pd.concat([application_pool, approved_case, approval_rate,average_wage], axis =1)
        industry_data.columns.values[0] = "application_pool"
        industry_data.columns.values[1] = "approved_case"
        industry_data.columns.values[2] = "approval_rate"
        industry_data.columns.values[3] = "average_wage"
    
        return industry_data

    def industry_application_pool(self, inductry_level, soc_name):
        return industry_level.newdf.ix[soc_name, "application_pool"]

    def industry_approved_case(self, inductry_level, soc_name):
        return industry_level.newdf.ix[soc_name, "approved_case"]
    
    def industry_approval_rate(self, inductry_level, soc_name):
        return industry_level.newdf.ix[soc_name, "approval_rate"]
    
    def industry_average_wage(self, inductry_level, soc_name):
        return industry_level.newdf.ix[soc_name, "average_wage"]
    
    def occupation_rank(self, inductry_level, n, indicator): 
        occupation_rank = industry_level.newdf.sort_values(by = indicator, ascending = False).ix[:n,indicator]
        return occupation_rank
    
'''
company level

'''

class company_level:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.newdf = company_level.company(self, dataset)

    def company(self, dataset):
    # calculate required statistics
        application_pool = (dataset.groupby("EMPLOYER_NAME").count())["STATUS_APPROVE"]
        approved_case = (dataset.groupby("EMPLOYER_NAME").sum())["STATUS_APPROVE"]
        approval_rate = (dataset.groupby("EMPLOYER_NAME").mean())["STATUS_APPROVE"]
        average_wage = (dataset.groupby("EMPLOYER_NAME").mean())["PREVAILING_WAGE"]
    
    # create a new DataFrame and rename indexes
        company_data = pd.concat([application_pool, approved_case, approval_rate,average_wage], axis =1)
        company_data.columns.values[0] = "application_pool"
        company_data.columns.values[1] = "approved_case"
        company_data.columns.values[2] = "approval_rate"
        company_data.columns.values[3] = "average_wage"
    
        return company_data

    def company_application_pool(self, company_level, company_name):
        return company_level.newdf.ix[company_name, "application_pool"]

    def company_approved_case(self, company_level, company_name):
        return company_level.newdf.ix[company_name, "approved_case"]
    
    def company_approval_rate(self, company_level, company_name):
        return company_level.newdf.ix[company_name, "approval_rate"]
    
    def company_average_wage(self, company_level, company_name):
        return company_level.newdf.ix[company_name, "average_wage"]
    
    def company_rank(self, company_level, n, indicator): 
        company_rank = company_level.newdf.sort_values(by = indicator, ascending = False).ix[:n,indicator]
        return company_rank    
    

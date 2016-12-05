'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt

'''
company_data = company_level(merged_data)
popular_company(company_data) 
'''


def popular_company(data):
    
    company_rank = data.newdf.sort_values(by = "application_pool", ascending = False).ix[:10]
    
    company_rank["unapproved_case"] = company_rank["application_pool"]-company_rank["approved_case"]

    print("The top 1o companies with largest application pools from 2010 to 2016 is ranked below: \n")
    print(company_rank.ix[:,0:1])

    fig1 = plt.figure(figsize = (30,10))
    ax1 = company_rank[["approved_case", "unapproved_case"]].plot(kind = "bar", alpha = 0.7, stacked = True,
                                                    figsize=(15, 8),title = "Approval Rate for Top 20 Largest Application Pool Companies")
    ax2 = company_rank["approval_rate"].plot(kind = "line", secondary_y=True, style = 'ko--' ,figsize=(15, 8))
    ax1.set_xticklabels(company_rank.index,rotation=75)
    ax2.set_xticklabels(company_rank.index,rotation=75)


    fig2 = plt.figure(figsize = (30,10))
    ax3 = company_rank["average_wage"].plot(kind = "bar", ylim = [40000,120000], figsize=(15, 8),
                              title ="Average Wage for Top 20 Largest Application Pool Companies" )
    ax3.set_xticklabels(company_rank.index,rotation=75)

    print(fig1)
    print(fig2)
    print("please return to the previous dictionary to explore other functions\n")
    
    return


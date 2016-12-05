'''
Created on Nov 27, 2016

@author: Yovela
'''
import sys
import pandas as pd
import matplotlib.pyplot as plt
from class_collections_ranking import *

'''
data = {}
for year in range(2010,2017):
    data[year]= pd.read_csv('Database/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
'''   

def city_exploring(data):
    
    merged_data = pd.concat([data[year] for year in range(2010,2017)], ignore_index= True)
    city_data = city_level(merged_data)
    
    city_rank = city_data.newdf.sort_values(by = "application_pool", ascending = False).ix[:20]
    city_rank["unapproved_case"] = city_rank["application_pool"]-city_rank["approved_case"]

    print("The top 20 cities with largest application pools from 2010 to 2016 is ranked below: \n")
    print(city_rank.ix[:,0:1])

    fig1 = plt.figure(figsize = (30,10))
    ax1 = city_rank[["approved_case", "unapproved_case"]].plot(kind = "bar", alpha = 0.7, stacked = True,
                                                    figsize=(15, 8),title = "Approval Rate for Top 20 Largest Application Pool Cities")
    ax2 = city_rank["approval_rate"].plot(kind = "line", secondary_y=True, style = 'ko--' ,figsize=(15, 8))
    ax1.set_xticklabels(city_rank.index,rotation=45)
    ax2.set_xticklabels(city_rank.index,rotation=45)


    fig2 = plt.figure(figsize = (30,10))
    ax3 = city_rank["average_wage"].plot(kind = "bar", ylim = [40000,120000], figsize=(15, 8),
                              title ="Average Wage for Top 20 Largest Application Pool Cities" )
    ax3.set_xticklabels(city_rank.index,rotation=45)

    print(fig1)
    print(fig2)
    print("please return to the previous dictionary to explore other functions\n") 

    return


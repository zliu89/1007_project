import sys
import pandas as pd

from h1b_data import *

from Country_Level import national_level
from State_Level import state_level
from city_exploring import city_exploring

from exception_list import wrong_option_exception
from Overview import option_input


data = {}
for year in range(2010,2017):
	data[year]= pd.read_csv('/Users/yuweitu/Documents/Programming/DSGA1007_Project/Database/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')

def location (df):
	df = h1b_data(df)
	
	Flag = True
	while Flag:
		try:
			print ("================================ H1b Visa Approve Rate Exploring ================================")
			print ("")
			print ("                             Please choose ONE level you interested in                           ")
			print ("                              <a>  : National Level                                              ")
			print ("                              <b>  : State Level                                                 ")
			print ("                              <c>  : City Level                                                  ")
			print ("                              <r>  : Go back to previous directory                               ")  
			print ("")
			print ("=================================================================================================")
			
			key = option_input()
			
			if key == 'a':
				national_level(df)
			if key == 'b':
				state_level(df.states, df)
			if key == 'c':
				city_exploring(df.data)
			if key == 'r':
				Flag = False

		except wrong_option_exception:
			print ("Invalid option, please reselect.")
			
location(data)
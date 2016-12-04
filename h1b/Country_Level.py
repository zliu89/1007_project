"""
This is module mainly focus on country level interaction

Created on 2016/12/01
Version: 1.0
@author: Sheng Liu
ShengLiu Copyright 2016-2017

"""
import sys
from Overview import option_input
from h1b_draw import *
from h1b_data import *


def national_level (h1b_data):
	#df = h1b_data(df)
	print ("  ")
	print ("================================ H1b Visa Approve Rate Exploring =================================")
	print ("")
	print ("          You are now at National Level, please choose ONE topic you interested in                ")
	print ("                              <a>  : Application Pool                                             ")
	print ("                              <b>  : Approve Rate                                                 ")
	print ("                              <c>  : Average Wage                                                 ")
	print ("                              <r>  : Return to Location Menu                                      ")
	print ("                      WARNING: For Year Input : Only 2010 ~ 2016                                  ")    
	print ("")
	print ("==================================================================================================")
	Flag = True

	while Flag:
		try:
			key = option_input()
			if key == 'a':
				year = input('Please input the year you are interested in: ')
				if year in ['2010','2011','2012','2013','2014','2015','2016']:
					year = int(year)
					application_pool = h1b_data.calc_application_pool('Country',year)
					plot_cloropleth_map(application_pool,'Application Pool','Pool Size',year)
					print("The information you requested has been saved, please use browser to open it...")
				elif year == 'quit':
					sys.exit(1)
				else:
					raise wrong_option_exception
			if key == 'b':
				year = input('Please input the year you are interested in: ')
				if year in ['2010','2011','2012','2013','2014','2015','2016']:
					year = int(year)
					APPROVE_RATE_LIST_Country = h1b_data.calc_approve_rate('Country',year)
					plot_cloropleth_map(APPROVE_RATE_LIST_Country,'Approve Rate','approve rate (%)',year)
					print("The information you requested has been saved, please use browser to open it...")
				elif year == 'quit':
					sys.exit(1)
				else:
					raise wrong_option_exception
			if key == 'c':
				year = input('Please input the year you are interested in: ')
				if year in ['2010','2011','2012','2013','2014','2015','2016']:
					AVERAGE_WAGE_LIST_Country = h1b_data.calc_average_wage('Country',int(year))
					plot_cloropleth_map(AVERAGE_WAGE_LIST_Country,'Average Wage','average wage ($)',int(year))
					print("The information you requested has been saved, please use browser to open it...")
				elif year == 'quit':
					sys.exit(1)
				else:
					raise wrong_option_exception
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")

if __name__ == '__main__':
	data = {}
	for year in range(2010,2017):
		data[year]= pd.read_csv('DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
	data = h1b_data(data)
	national_level(data)


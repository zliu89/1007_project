"""
This is the Overall module of the project, in this module, we focus on which topic a customer interested in.

Author: ShengLiu (sl5924)
"""

import sys
from h1b_draw import *
import h1b_data
def overview(data):
	data = h1b_data(data,)
	print ("================================ H1b Visa Approve Rate Exploring ================================")
	print ("")
	print ("                             Please choose one topic you interested in                           ")
	print ("                              <a>  : Application Pool                                            ")
	print ("                              <b>  : Approval Rate                                               ")
	print ("                              <c>  : Average Wage                                                ")
	print ("                              <r>  : Go back to previous directory                               ")  
	print ("")
	print ("=================================================================================================")
	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				application_pool = calc_application_pool('Overview')
				plot_line_chart(application_pool,'Application Pool Size','Overview of Application Pool')
				
			if key == 'b':
				APPROVE_RATE_LIST = calc_approve_rate('Overview')
				plot_line_chart(APPROVE_RATE_LIST,'Approve Rate (%)','Overview of Approve Rate')
			
			if key == 'c':
				df.plot_wage_line_chart()
			
			if key == 'r':
				Flag = False
		
		except KeyboardInterrupt:
			sys.exit(1)
		except wrong_option_exception:
			print ("Invalid option, please reselect.")


def option_input():

	key = input("Please select one: ")
	options = list('abcr')
	if not(key in options):
		raise wrong_option_exception
	if key == 'quit':
		print ("You have quited the system.")
		sys.exit()
	return key




import sys
from Overview import option_input
def national_level (df):
	#df = h1b_data(df)

	print ("================================ H1b Visa Approve Rate Exploring =================================")
	print ("")
	print ("          You are now at National Level, please choose ONE topic you interested in                ")
	print ("                              <a>  : Application Pull                                             ")
	print ("                              <b>  : Approve Rate                                                 ")
	print ("                              <c>  : Average Wage                                                 ")
	print ("                              <r>  : Return to Location Menu                                      ")  
	print ("")
	print ("==================================================================================================")
	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				df.plot_application_map('national')
			if key == 'b':
				df.plot_approve_map('national')
			if key == 'c':
				df.plot_wage_map('national')
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")
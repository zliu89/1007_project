import sys
from h1b_data import *
def state_level (df):
	#df = h1b_data(df)

	print ("================================ H1b Visa Approve Rate Exploring =================================")
	print ("")
	print ("          Please Input a state ABBREVIATION you interested in (NY, CA, MI, etc.)                  ")
	print ("		             You may input return to go back to Location menu                             ")			
	print ("==================================================================================================")

	state_name = input('Please input here: ') 
	while True
		if state_name in df.states:
			df.plot_application_line_chart(state_name)
			df.plot_approve_line_chart(state_name)
			df.plot_wage_line_cahrt(state_name)
			rank = df.top10_rank()
			#How do we show the rank if the rank is acturally a data frame
		elif state_name == 'return':
			break
		else:
			raise Exception







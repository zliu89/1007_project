import sys
from Overview import option_input
from h1b_data import *
def city_level (df):
	#df = h1b_data(df)
	print ("================================ H1b Visa Approve Rate Exploring ================================")
	print ("")
	print ("               You are now in city level, please choose ONE aspect you interested in                           ")
	print ("                              <a>  : Top 20 largest application pulls                            ")
	print ("                              <b>  : Top 20 highest approval rate                                ")
	print ("                              <c>  : Top 20 highest average wage                                 ")
	print ("                              <r>  : Go back to previous directory                               ")  
	print ("")
	print ("=================================================================================================")

	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				df.top10_rank()
			if key == 'b':
				df.top10_rank()
			if key == 'c':
				df.top10_rank()
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")
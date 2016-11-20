from h1b_data import *
def popular_industry (df):
	

	print ("================================ H1b Visa Approve Rate Exploring ================================")
	print ("")
	print ("                             Please choose ONE topic you interested in                           ")
	print ("                              <a>  : Application Pull                                            ")
	print ("                              <b>  : Approve Rate                                                ")
	print ("                              <c>  : Average Wage                                                ")
	print ("                              <r>  : Go back to previous directory                               ")  
	print ("")
	print ("=================================================================================================")
	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				df.top_rank(10, , )
			if key == 'b':
				df.top_rank(10, , )
			if key == 'c':
				df.top_rank(10, , )
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")
import sys

def location (df):
	df = h1b_data(df)

	print ("================================ H1b Visa Approve Rate Exploring ================================")
	print ("")
	print ("                             Please choose ONE level you interested in                           ")
	print ("                              <a>  : Popular Industry                                            ")
	print ("                              <b>  : Customized Job Inquiry                                      ")
	print ("                              <r>  : Go back to main menu                                        ")  
	print ("")
	print ("=================================================================================================")
	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				popular_industry()
			if key == 'b':
				customized()
			if key == 'c':
				city_level()
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")
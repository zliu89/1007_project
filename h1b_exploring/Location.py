import sys
def location (df):
	df = h1b_data(df)

	print ("================================ H1b Visa Approve Rate Exploring ================================")
	print ("")
	print ("                             Please choose ONE level you interested in                           ")
	print ("                              <a>  : National Level                                              ")
	print ("                              <b>  : State Level                                                 ")
	print ("                              <c>  : City Level                                                  ")
	print ("                              <r>  : Go back to previous directory                               ")  
	print ("")
	print ("=================================================================================================")
	Flag = True
	while Flag:
		try:
			key = option_input()
			if key == 'a':
				national_level(df)
			if key == 'b':
				state_level(df)
			if key == 'c':
				city_level(df)
			if key == 'r':
				Flag = False
		except wrong_option_exception:
			print ("Invalid option, please reselect.")
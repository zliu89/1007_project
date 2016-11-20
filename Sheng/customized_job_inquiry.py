def customized (df):
	
	while True:
		try:
			print ("================================ H1b Visa Approve Rate Exploring ================================")
			print ("")
			company_name = input ("                      Please Input Your Interested Company Name                          ")
			print ("")
			print ("=================================================================================================")
			company_name = df.identify_company_name()
			input("Are you intersted in %s",company_name)
			
		except Invalid_Company_Name:
			print ("Invalid company name, please input agein")

	df.search_company(company_name)
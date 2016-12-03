import sys
import pandas as pd
import h1b_draw
class h1b_data:
	def __init__(self,year):
		self.data = pd.read_excel('H-1B_FY2016.xlsx')
		self.states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', \
         'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', \
         'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', \
         'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',\
         'VA', 'WA', 'WV', 'WI', 'WY']




	def calc_approve_rate(self,level):
		if level == 'states':
			APPROVE_RATE_DIC = {}
			APPRIVE_RATE_LIST = []
			df = self.data
			for state in self.states:
		    	df_in_state = df[df['EMPLOYER_STATE']== state]
	    		is_approve = (df_in_state['CASE_STATUS']=='CERTIFIED')*1
	    		APPROVE_RATE_DIC[state] = sum(is_approve)/len(df_in_state)
	    		APPRIVE_RATE_LIST.append(sum(is_approve)/len(df_in_state)*100)
				state_data = pd.DataFrame.from_dict(APPROVE_RATE_DIC,orient='index',dtype=None)
				state_data = state_data.rename(columns = {0:'approve_percentage'})
				state_data.to_csv(path_or_buf = '../mystuff/HW1007/2016_approve_percentage.csv')
			return state_data
		elif level == 'national':


		elif level == 'city':

		else:
		 raise Wrong_Level_Input_Exception






	def calc_applicaton_pull(self,level):

	def calc_applicaton_pull_state(self,state_name):


	def calc_approve_rate_state(self,state_name):

	def calc_average_wage_state(self,state_name):





	def calc_average_wage(self,level):


	def plot_application_line_chart(self,state_name):
		if state_name == None:
			try:
				data = self.calc_applicaton_pull('national')
				h1b_draw.plot_line_chart(data)
			except Wrong_Level_Input_Exception:
				print ('Invalid Level')
		else:
			data = self.calc_applicaton_pull_state(state_name)
			h1b_draw.plot_line_chart(data)


	def plot_approve_line_chart(self,state_name):
		if state_name == None:
			data = self.calc_approve_rate('national')
			h1b_draw.plot_line_chart(data)
		else:
			data = self.calc_approve_rate_state(state_name)
			h1b_draw.plot_line_chart(data)	


	def plot_wage_line_cahrt(self,state_name):
		if state_name == None
			data = self.calc_average_wage('national')
			h1b_draw.plot_line_chart(data)
		else:
			data = self.calc_average_wage_state(state_name)
			h1b_draw.plot_line_chart(data)


	def plot_application_map(self,level):
		if level == 'national':
			data = self.calc_national_applicaton_pull()
			h1b_draw.plot

	def plot_approve_map(self,level):


	def plot_wage_map(self,level):



	def top_rank(self,top,kind,type):
	"""
	Input: 
		top: 10 or 20
		kind: company or occupation or city
		type: approval rate or average wage or application pull

	Return:
		Required rank (data frame)
    """
    def identify_company_name(self,company_name):
    """
	Input:
		company_name

	Return:
		identified company_name(string) based on the data base

	Exception:
		Invalid_Company_Name
    """
    
    def search_company(self,company_name):

	"""
	Input: company_name

	Output:
	campany_name
	Group name
	Sub-group list
	application pull from 2009-2016
	approval rate from 2009-2016
	average rate from 2009-2016









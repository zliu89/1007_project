import sys
import pandas as pd
from chorogrid import Colorbin, Chorogrid
from h1b_data import h1b_data
class h1b_draw:
	def __init__(self,map_type,year,state):
        '''
        Constructor
        '''
        try:
        	self.year = year
            if map_type in [1,2,3]:
                
         		self.mycolors = ['#b35806', '#f1a340', '#fee0b6', '#d8daeb', '#998ec3', '#542788']
         		state_data = h1b_data.calc_states_approve_rate(year)
         		self.mybin = Colorbin(state_data['approve_percentage'], mycolors, proportional=True, decimals=None)
         		self.state_info = pd.read_csv('chorogrid/databases/usa_states.csv')
         		self.map_type = map_type
         		
            elif state != '':
            	self.data = h1b_data.calc_city_approve_rate(year,state)
            	self.position = arange(5)+.5  
            	self.val = self.data.
        except Exception:
            raise              
        


    

    def plot_cloropleth_map(self):
    	#self.mybin.set_decimals(1)
		#self.mybin.recalc(fenceposts=True)
		#self.mybin.calc_complements(0.5, '#e0e0e0', '#101010')
		if self.map_type == 1:
			colors_by_state = self.mybin.colors_out
			font_colors_by_state = self.mybin.complements
			legend_colors = self.mybin.colors_in
			legend_labels = self.mybin.labels
			cg = Chorogrid('chorogrid/databases/usa_states.csv', states, colors_by_state)
			cg.set_title('% 2016 H1b Approve Rate', font_dict={'font-size': 19})
			cg.set_legend(legend_colors, legend_labels, title='% of population')
			cg.draw_squares(spacing_dict={'margin_right': 150}) # otherwise legend will be cut off
	    # another strategy would be to pass a legend_offset to spacing_dict
			cg.done(show=True)
		elif self.map_type == 2:
			cg = Chorogrid('chorogrid/databases/usa_states.csv', states, colors_by_state)
			cg.draw_map(spacing_dict={'legend_offset': [-150,-25]})
			cg.done(show=True)
		else:
			cg.draw_hex(spacing_dict={'margin_right': 150}, font_colors=font_colors_by_state)
			cg.done(show=True)



	def plot_bar_chart(self):
		val = self.val
		barh(self.position,val, align='center',height=0.1)    # notice the 'height' argument
		yticks(pos, ('Tom', 'Dick', 'Harry', 'Slim', 'Jim'))
		xlabel('Approve Rate')
		title('Approve Rate of Top 20 Cities in'+str(state))
		grid(True)
		show()











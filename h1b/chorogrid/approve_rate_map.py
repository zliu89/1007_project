from chorogrid import Colorbin, Chorogrid
import pandas as pd
df = pd.read_excel('H-1B_FY2016.xlsx')
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
APPROVE_RATE_DIC = {}
APPRIVE_RATE_LIST = []
for state in states:
    df_in_state = df[df['EMPLOYER_STATE']== state]
    is_approve = (df_in_state['CASE_STATUS']=='CERTIFIED')*1
    APPROVE_RATE_DIC[state] = sum(is_approve)/len(df_in_state)
    APPRIVE_RATE_LIST.append(sum(is_approve)/len(df_in_state)*100)
state_data = pd.DataFrame.from_dict(APPROVE_RATE_DIC,orient='index',dtype=None)
state_data = state_data.rename(columns = {0:'approve_percentage'})
mycolors = ['#b35806', '#f1a340', '#fee0b6', '#d8daeb', '#998ec3', '#542788']

mybin = Colorbin(state_data['approve_percentage'], mycolors, proportional=True, decimals=None)
mybin.set_decimals(1)
mybin.recalc(fenceposts=True)
mybin.calc_complements(0.5, '#e0e0e0', '#101010')
colors_by_state = mybin.colors_out
font_colors_by_state = mybin.complements
legend_colors = mybin.colors_in
legend_labels = mybin.labels

cg = Chorogrid('chorogrid/databases/usa_states.csv', states, colors_by_state)
cg.set_title('% 2016 H1b Approve Rate', font_dict={'font-size': 19})
cg.set_legend(legend_colors, legend_labels, title='% of population')
cg.draw_squares(spacing_dict={'margin_right': 150}) # otherwise legend will be cut off
    # another strategy would be to pass a legend_offset to spacing_dict
cg.done(show=True)

"""
This is the main module of the project, all the functions are imported from package H1b

Author:  ShengLiu (sl5924)
"""
import pandas as pd
from H1b import *
import sys


def main():
    """
    The whole project start here.
    """

    # start at loading the dataset
    raw_data = h1bdata_loading()
    print "dataset loaded successfully >>>"
    print ">>>",

    # Then clean the data
    h1b_data = Clean_df(raw_data)
    print "data cleaned >>>"

    merged_data = pd.concat([h1b_data[year] for year in range(2010,2017)], ignore_index= True)

    # search for interested jobs
    print ("================================ H1b Visa Approve Rate Exploring ================================")
	print (""
	print ("                             How do you want to explore the H1b Data?                            ")
	print ("                              <a>  : Overview                              		                 ")
	print ("                              <b>  : Location                                                    ")
	print ("                              <c>  : Industry                                                    ")
	print ("                              <d>  : Company                                                     ")  
	print ("")
	print ("=================================================================================================")
	while True:
		try:
			key = option_input()
			if key == 'a':
				overview(h1b_data)
			if key == 'b':
				location(h1b_data)
			if key == 'c':
				industry_exploring(merged_data)
			if key == 'd':
				company_exploring(merged_data)
		except wrong_option_exception:
			print ("Invalid option, please reselect.")













    job_list, keyword = overall_analysis(job_data)
    "Matching >>>"

    # analysis this job list
    if type(job_list) == pd.DataFrame:
        job_list_analysis(job_list, keyword)
    elif type(job_list) == pd.Series:
        one_job_info(job_list)
    # program end

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit()


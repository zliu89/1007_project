"""
This is module tests the methods in class h1b_data

Created on 2016/12/01
Version: 1.0
@author: Sheng Liu
ShengLiu Copyright 2016-2017
"""

from h1b_data import *
import unittest

class utest(unittest.TestCase):
	def setUp(self):
		pass

	def test_calc_application_pool(self):
		self.assertEqual(h1b_data(data).calc_application_pool('Overview',2016),[296960, 313562, 366692, 394943, 471646, 567927, 597356])
		country_List = [1176, 48, 3661, 1806, 94431, 3707, 6016, 1899, 1930,14320, 16774, 291, 604, 40704, 2929, 1767, 1796, 2305, 1295, 384, 20415, 21323, 21877, 4066, 485, 4551, 86, 1450, 826, 983, 84228, 718, 45838, 19497, 274, 9159, 884, 1551, 24343, 925, 1140, 230, 3899, 90550, 1629, 460, 18201, 16045, 342, 3003, 77]
		self.assertEqual(h1b_data(data).calc_application_pool('Country',2016),country_List)
		self.assertEqual(h1b_data(data).calc_application_pool('State','NY'),[30070, 27810, 28616, 27422, 31266, 35308, 45838])

	def test_calc_approve_rate(self):
		#self.assertEqual(h1b_data(data).calc_approve_rate('Overview',123),[1,2,3])
		

		









if __name__ == '__main__':
	data = {}
	for year in range(2010,2017):
		data[year]= pd.read_csv('DataBase/H-1B_FY'+str(year)+'_clean.csv',encoding = 'iso-8859-1')
	unittest.main()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class qxTest(unittest.TestCase):
	'''权限-充值测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_cw(self):
		pass

		#验证错误拦截项




	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_wldw import wldw

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#导入正确
		wldw(self.driver).user_login()

	def test_2kehu(self):
		#导入正确
		wldw(self.driver).user_login()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



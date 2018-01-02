from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_tjbb import tjbb
from page_obj.pc_daoru import daoru

class qxTest(unittest.TestCase):
	'''权限-应收报表测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1mingxi(self):
		daoru(self.driver).user_login_xh()

if __name__ == '__main__':
	unittest.main()




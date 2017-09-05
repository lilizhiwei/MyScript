from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_gjqx import gjqx
from page_obj.pc_daoru import daoru

class loginTest(unittest.TestCase):
	'''权限-员工测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1mima(self):
		daoru(self.driver).user_login_xh()
		#修改权限
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_mima()
		gjqx(self.driver).clickbc()

		#验证1
		
	def test_2tingyong(self):
		daoru(self.driver).user_login_xh()

		#验证1
		
		#修改权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_mima()
		gjqx(self.driver).yg_tingyong()
		gjqx(self.driver).clickbc()

		#验证2
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



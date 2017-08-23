from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("./page")
from page.page_lianxiren import login

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		login(self.driver).user_login()
		login(self.driver).clicklianxiren()
		login(self.driver).xzkh()
		login(self.driver).tjgdx()
		login(self.driver).fenzu()
		login(self.driver).tjgdx1()
		login(self.driver).fuzeren()
		login(self.driver).tjgdx1()
		login(self.driver).dqqk()
		login(self.driver).typeuser()
		login(self.driver).typeqk(99)
		sleep(5)

		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



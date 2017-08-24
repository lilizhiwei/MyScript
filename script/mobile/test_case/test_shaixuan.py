from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.mobile_lianxiren import shaixuan

class loginTest(unittest.TestCase):
	'''筛选功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#创建一个未分组，负责人老板，有欠款
		shaixuan(self.driver).user_login()
		shaixuan(self.driver).openmobile()
		shaixuan(self.driver).clicklianxiren()
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		shaixuan(self.driver).typeuser()
		shaixuan(self.driver).typeqk(100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#创建一个有分组，负责人营业员，有预存
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fenzu()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		shaixuan(self.driver).typeuser()
		shaixuan(self.driver).clickfenzu()
		shaixuan(self.driver).clickfuzeren()
		shaixuan(self.driver).typeqk(-100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()
		sleep(5)
		#筛选

		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



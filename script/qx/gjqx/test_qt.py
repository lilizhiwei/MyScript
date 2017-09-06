from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_gjqx import gjqx
from page_obj.pc_daoru import daoru

class qxTest(unittest.TestCase):
	'''权限-其他'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1jiaojie(self):
		daoru(self.driver).user_login_xh()
		#修改权限
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).qt_jiaojie()
		gjqx(self.driver).clickbc()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("交接班历史").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".glist-tip")))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".glist-tip").text,'出错喇！权限不足')

	def test_2huanyuan(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='421']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='421']").get_attribute("class"))

		#还原权限
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).qt_jiaojie()
		gjqx(self.driver).clickbc()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



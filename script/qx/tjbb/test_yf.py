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
	'''权限-应付报表测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1mingxi(self):
		daoru(self.driver).user_login_xh()
		#修改权限
		tjbb(self.driver).clickyg()
		tjbb(self.driver).clickqx()
		tjbb(self.driver).clicktjbb()
		tjbb(self.driver).yf_mingxi()
		tjbb(self.driver).clickbc()

	def test_2chakan(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-pie-chart']").click()
		self.driver.find_element_by_link_text("应付报表").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@class="wrapcontainertr"]/tr/td')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@class="wrapcontainertr"]/tr/td').click()
		sleep(2)
		self.assertNotRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*应付详情[\s\S]*") 
	
		#修改权限
		tjbb(self.driver).clickyg()
		tjbb(self.driver).clickqx()
		tjbb(self.driver).clicktjbb()
		tjbb(self.driver).yf_mingxi()
		tjbb(self.driver).yf_chakan()
		tjbb(self.driver).clickbc()
		
	def test_3huanyuan(self):
		daoru(self.driver).user_login_xh()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-pie-chart']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='360']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='360']").get_attribute("class"))

		#修改权限
		tjbb(self.driver).clickyg()
		tjbb(self.driver).clickqx()
		tjbb(self.driver).clicktjbb()
		tjbb(self.driver).clickquanxuan_yf()
		tjbb(self.driver).clickbc()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()




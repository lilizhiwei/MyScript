from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_wldw import wldw

class loginTest(unittest.TestCase):
	'''权限-客户'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1jifen(self):
		#修改权限
		wldw(self.driver).user_login_xh()
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_jifen()
		wldw(self.driver).clickbc()

		#验证1
		wldw(self.driver).clickkehu()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='169']//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='169']//i").click()
		self.driver.find_element_by_xpath("//*[@data-action='addScore']/a").click()
		self.driver.find_element_by_xpath("//*[@placeholder='输入要增加的积分']").send_keys(10)
		self.driver.find_element_by_xpath("//*[@class='layui-layer-btn0']").click()
		wldw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_2gongxiang(self):
		wldw(self.driver).user_login_xh()

		#验证1
		wldw(self.driver).clickkehu()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='169']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='169']").get_attribute("class"))
	
		#创建一个无负责人客户
		
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_jifen()
		wldw(self.driver).qx_gongxiang()
		wldw(self.driver).clickbc()

		#验证2
		#有bug
		wldw(self.driver).clickkehu()


		sleep(1)

	def test_3daoru(self):
		wldw(self.driver).user_login_xh()

		#验证2
	
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_daoru()
		wldw(self.driver).qx_gongxiang()
		wldw(self.driver).clickbc()

		#验证3
		wldw(self.driver).clickkehu()


		sleep(2)

	def test_4shanchu(self):
		wldw(self.driver).user_login_xh()

		#验证3
	
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_daoru()
		#wldw(self.driver).qx_shanchu()
		wldw(self.driver).clickbc()

		#验证4
		wldw(self.driver).clickkehu()


		sleep(2)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()




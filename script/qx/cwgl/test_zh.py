from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_cwgl import cwgl
from page_obj.pc_daoru import daoru

class qxTest(unittest.TestCase):
	'''权限-资金账户测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1shanchu(self):
		daoru(self.driver).user_login_xh()
		#新增一个资金账户
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("新增资金帐户").click()
		self.driver.find_element_by_name("name").send_keys("建设")
		self.driver.find_element_by_id("save").send_keys(Keys.SPACE)
		sleep(1)

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).zh_shanchu()
		cwgl(self.driver).clickbc()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		self.driver.find_element_by_xpath("//tbody[@id='tbody']/tr[5]/td[4]/button[2]").click()
		self.driver.find_element_by_link_text("确定").click()
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_2xiugai(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//tbody[@id='tbody']/tr[5]/td[4]/button[2]")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//tbody[@id='tbody']/tr[5]/td[4]/button[2]").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		# cwgl(self.driver).zh_xiugai()
		cwgl(self.driver).zh_shanchu()
		cwgl(self.driver).clickbc()

		#验证2
		# self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		# self.driver.find_element_by_link_text("资金帐户").click()
		# self.driver.find_element_by_xpath("//tbody[@id='tbody']/tr[5]/td[4]/button").click()
		# WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.ID,"save")))
		# sleep(0.5)
		# self.driver.find_element_by_id("save").send_keys(Keys.SPACE)
		# cwgl(self.driver).qxbz()
		# self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_3xinzeng(self):
		daoru(self.driver).user_login_xh()

		# 验证2
		# self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		# self.driver.find_element_by_link_text("资金帐户").click()
		# WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//tbody[@id='tbody']/tr[5]/td[4]/button")))
		# sleep(0.5)
		# self.assertIn("hide",self.driver.find_element_by_xpath("//tbody[@id='tbody']/tr[5]/td[4]/button").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		# cwgl(self.driver).zh_xiugai()
		cwgl(self.driver).zh_xinzeng()
		cwgl(self.driver).clickbc()

		#验证3
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("新增资金帐户").click()
		self.driver.find_element_by_name("name").send_keys("建设")
		self.driver.find_element_by_id("save").send_keys(Keys.SPACE)
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_4chakan(self):
		daoru(self.driver).user_login_xh()

		#验证3
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='261']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='261']").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).zh_xinzeng()
		#cwgl(self.driver).zh_chakan()
		cwgl(self.driver).clickbc()

		#验证3
		

		#还原
		# cwgl(self.driver).clickyg()
		# cwgl(self.driver).clickqx()
		# cwgl(self.driver).clickcwgl()
		# cwgl(self.driver).clickquanxuan_zh()
		# cwgl(self.driver).clickbc()
	
		#删除账户建设 	
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		self.driver.find_element_by_xpath("//tbody[@id='tbody']/tr[5]/td[4]/button[2]").click()
		self.driver.find_element_by_link_text("确定").click()
		sleep(1)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



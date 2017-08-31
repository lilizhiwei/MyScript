from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_spyw import spyw
from page_obj.pc_daoru import daoru

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1shanchu(self):
		daoru(self.driver).user_login_xh()
		#新增一个销售退货单
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("新增销售单").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.ID,"inputHorizontalFemale")))
		sleep(2)
		self.driver.find_element_by_id("inputHorizontalFemale").send_keys(Keys.SPACE)
		sleep(1)
		self.driver.find_element_by_xpath("//*[@id='1']/td[3]").click()
		self.driver.find_element_by_xpath("//*[@id='1']/td[3]/div/span[2]").click()
		sleep(1)
		self.driver.find_element_by_xpath("//tbody//input[@type='checkbox']").click()
		sleep(1)
		self.driver.find_element_by_link_text("确定").click()
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li[3]/a[@class='bg-blue-600 white submit']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"保存成功"))
		sleep(0.5)

		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).xs_shanchu()
		spyw(self.driver).clickbc()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("销售历史").click()
		self.driver.find_element_by_css_selector(".number").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='删除']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='删除']").click()
		self.driver.find_element_by_link_text("确定").click()
		spyw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_2xiugai(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("销售历史").click()
		self.driver.find_element_by_css_selector(".number").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='dropdown padding-right-10 hide']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@class='dropdown padding-right-10 hide']").get_attribute("class"))

		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).xs_shanchu()
		spyw(self.driver).xs_xiugai()
		spyw(self.driver).clickbc()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("销售历史").click()
		self.driver.find_element_by_css_selector(".number").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='编辑']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='编辑']").click()
		self.driver.find_element_by_link_text("确定").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//ul/li[3]/a[@class='bg-blue-600 white submit']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li[3]/a[@class='bg-blue-600 white submit']").click()
		spyw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_3xinzeng(self):
		daoru(self.driver).user_login_xh()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("销售历史").click()
		self.driver.find_element_by_css_selector(".number").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='dropdown padding-right-10 hide']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@class='dropdown padding-right-10 hide']").get_attribute("class"))

		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).xs_xiugai()
		spyw(self.driver).xs_xinzeng()
		spyw(self.driver).clickbc()

		#验证3
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("新增销售单").click()
		self.driver.find_element_by_xpath("//*[@id='1']/td[3]").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-ac-menu-index='0']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-ac-menu-index='0']").click()
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li[3]/a[@class='bg-blue-600 white submit']").click()
		spyw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_4chakan(self):
		daoru(self.driver).user_login_xh()

		#验证3
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='102']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='102']").get_attribute("class"))

		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).xs_xinzeng()
		spyw(self.driver).xs_chakan()
		spyw(self.driver).clickbc()

		#验证4
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("销售历史").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".glist-tip>.text-center.border-bottom-0")))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".glist-tip>.text-center.border-bottom-0").text,"出错喇！权限不足")
		
		#还原
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).clickquanxuan_xsd()
		spyw(self.driver).clickbc()


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



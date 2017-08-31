from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_wldw import wldw
from page_obj.pc_daoru import daoru

class loginTest(unittest.TestCase):
	'''权限-供货商'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_2gongxiang(self):
		wldw(self.driver).user_login_xh()
	
		#创建一个无负责人客户
		
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_gongxiang()
		wldw(self.driver).clickbc()

		#验证2
		#有bug
		daoru(self.driver).clickghs()


		sleep(1)

	def test_3daoru(self):
		wldw(self.driver).user_login_xh()

		#验证2
	
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_daoru()
		wldw(self.driver).qx_ghs_gongxiang()
		wldw(self.driver).clickbc()

		#验证3
		daoru(self.driver).clickghs()
		daoru(self.driver).clickX()
		daoru(self.driver).clickdaoru2()
		daoru(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lq.exe")
		daoru(self.driver).clicktijiao()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content"),"权限不足"))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content").text,'权限不足')
		self.driver.find_element_by_link_text("确定").click()

	def test_4shanchu(self):
		wldw(self.driver).user_login_xh()

		#验证3
		daoru(self.driver).clickghs()
		daoru(self.driver).clickX()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='176']")))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_xpath("//*[@data-power='176']").get_attribute("class"),"hide")

		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_daoru()
		wldw(self.driver).qx_ghs_shanchu()
		wldw(self.driver).clickbc()

		#验证4
		daoru(self.driver).clickghs()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='删除']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='删除']").click()
		self.driver.find_element_by_link_text("确定").click()
		wldw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_5xiugai(self):
		wldw(self.driver).user_login_xh()

		#验证4
		daoru(self.driver).clickghs()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='173']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='173']").get_attribute("class"))

		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_xiugai()
		wldw(self.driver).qx_ghs_shanchu()
		wldw(self.driver).clickbc()

		#验证5
		daoru(self.driver).clickghs()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='编辑']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='编辑']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//span[text()='大屏展示']/../span")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//span[text()='大屏展示']/../span").click()
		wldw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_6xinzeng(self):
		wldw(self.driver).user_login_xh()

		#验证5
		daoru(self.driver).clickghs()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='172']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='172']").get_attribute("class"))

		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_xiugai()
		wldw(self.driver).qx_ghs_xinzeng()
		wldw(self.driver).clickbc()

		#验证6
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("新增供货商").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-role='cname']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-role='cname']").send_keys("李志伟")
		self.driver.find_element_by_xpath("//span[text()='大屏展示']/../span").click()
		wldw(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_7chakan(self):
		wldw(self.driver).user_login_xh()

		#验证6
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='171']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='171']").get_attribute("class"))
		
		#修改权限
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).qx_ghs_xinzeng()
		wldw(self.driver).qx_ghs_chakan()
		wldw(self.driver).clickbc()

		#验证7
		daoru(self.driver).clickghs()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".glist-tip>.text-center")))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".glist-tip>.text-center").text,"出错喇！权限不足")

		#还原
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		wldw(self.driver).clickwldw()
		wldw(self.driver).clickquanxuan_ghs()
		wldw(self.driver).clickbc()
		sleep(1)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
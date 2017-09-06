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
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='405']")))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="405"]').click()
		self.driver.find_element_by_css_selector(".input-group.input-group-icon > input.form-control").send_keys("13523148316")
		self.driver.find_element_by_css_selector(".form-group.margin-bottom-0 > div.input-group.input-group-icon > input.form-control").send_keys("123456")
		self.driver.find_element_by_link_text("确定").click()
		gjqx(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_2tingyong(self):
		daoru(self.driver).user_login_xh()

		#验证1
		gjqx(self.driver).clickyg()
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='405']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='405']").get_attribute("class"))

		#修改权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_mima()
		gjqx(self.driver).yg_tingyong()
		gjqx(self.driver).clickbc()

		#验证2
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-tips-title="离职"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-tips-title="离职"]').click()
		self.driver.find_element_by_link_text("确定").click()
		gjqx(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_3shanchu(self):
		daoru(self.driver).user_login_xh()

		#验证1
		gjqx(self.driver).clickyg()
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='404']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='404']").get_attribute("class"))

		#修改权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_tingyong()
		gjqx(self.driver).yg_shanchu()
		gjqx(self.driver).clickbc()

		#验证2
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-tips-title="删除"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-tips-title="删除"]').click()
		self.driver.find_element_by_link_text("确定").click()
		gjqx(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_4xiugai(self):
		daoru(self.driver).user_login_xh()

		#验证1
		gjqx(self.driver).clickyg()
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='403']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='403']").get_attribute("class"))

		#修改权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_shanchu()
		gjqx(self.driver).yg_xiugai()
		gjqx(self.driver).clickbc()

		#验证2
		self.driver.refresh()
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-tips-title="编辑"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-tips-title="编辑"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-action="save"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-action="save"]').click()
		gjqx(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_5xinzeng(self):
		daoru(self.driver).user_login_xh()

		#验证1
		gjqx(self.driver).clickyg()
		self.driver.refresh()
		sleep(0.5)
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".panel-body > div.media > div.media-left > img.img-circle")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".panel-body > div.media > div.media-left > img.img-circle").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='402']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='402']").get_attribute("class"))

		#修改权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_xinzeng()
		gjqx(self.driver).yg_xiugai()
		gjqx(self.driver).clickbc()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("新增员工").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="姓名"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@placeholder='姓名']").send_keys("李李李志伟")
		self.driver.find_element_by_xpath('//*[@data-action="save"]').click()
		gjqx(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_6chakan(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='401']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='401']").get_attribute("class"))

		#修改权限
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).yg_xinzeng()
		gjqx(self.driver).yg_chakan()
		gjqx(self.driver).clickbc()

		#验证2
		self.driver.refresh()
		sleep(0.5)
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.media-heading.text-truncate')))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".media-heading.text-truncate").text,'李志伟小号')
		sleep(1)

		#还原权限
		daoru(self.driver).clicksp()
		gjqx(self.driver).clickyg()
		gjqx(self.driver).clickqx()
		gjqx(self.driver).clickgjqx()
		gjqx(self.driver).clickquanxuan_yg()
		gjqx(self.driver).clickbc()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



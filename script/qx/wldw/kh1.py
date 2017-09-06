from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_wldw import wldw

class qxTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#打开第一页面
		wldw(self.driver).user_login()
		wldw(self.driver).clickyg()
		wldw(self.driver).clickqx()
		#获取第一页面handle信息
		sreach_windows = self.driver.current_window_handle

		#打开第二页面
		wldw(self.driver).openxh()

		#获取所有页面信息
		all_handles = self.driver.window_handles
		#切到第二页面
		for handle in all_handles:
			if handle != sreach_windows:
				self.driver.switch_to.window(handle)
				sleep(5)

		wldw(self.driver).user_login_xh()

		#切回第一页面
		for handle in all_handles:
			if handle == sreach_windows:
				self.driver.switch_to.window(handle)
				sleep(5)

		#修改权限
		



		#切回第二页面
		for handle in all_handles:
			if handle != sreach_windows:
				self.driver.switch_to.window(handle)
				sleep(5)

		#验证
		

	def test_2kehu(self):
		#导入正确
		wldw(self.driver).user_login()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



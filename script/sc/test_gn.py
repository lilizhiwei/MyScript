from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class qxTest(unittest.TestCase):
	'''权限-充值测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_cw(self):
		#创建数据，然后pc端关闭功能，然后商城验证，最后pc端还原
		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '商品1' + str(b)
		sc(self.driver).cj_sp1(name2)
		sc(self.driver).sp_sj(name4)
		#上架
		self.driver.find_element_by_css_selector('.lcs_cursor').click()

		#关闭商店开关
		sc(self.driver).sp_sj()


		#商城验证
		sc(self.driver).opensc()

		




	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
	
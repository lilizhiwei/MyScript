from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os,random
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class qxTest(unittest.TestCase):
	'''商城-搜索筛选测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_sx(self):
		
		#pc端创建商品
		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		bh1 = str(a) + str(b)
		name2 = str(a) + '商品1' + str(b)
		name3 = str(a) + '商品2' + str(b)
		name4 = str(a) + '套餐' + str(b)
		fl1 = str(a) + '大类' + str(b)
		fl2 = str(a) + '小类' + str(b)
		sc(self.driver).cj_kh(name1,bh1)
		sc(self.driver).cj_sp1(name2)
		sc(self.driver).cj_sp3(name3,fl1,fl2)
		sc(self.driver).cj_tc(name4)
		sc(self.driver).sp_sj(name4)

		#商城验证

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



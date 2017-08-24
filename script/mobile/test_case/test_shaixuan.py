from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os,random
sys.path.append("../../page_obj")
from page_obj.mobile_lianxiren import shaixuan

class loginTest(unittest.TestCase):
	'''筛选功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#创建一个未分组，负责人老板，有欠款
		shaixuan(self.driver).user_login()
		shaixuan(self.driver).openmobile()
		shaixuan(self.driver).clicklianxiren()
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser(name1)
		shaixuan(self.driver).typeqk(100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#创建一个有分组，负责人营业员，有预存
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fenzu()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser(name2)
		shaixuan(self.driver).clickfenzu()
		shaixuan(self.driver).clickfuzeren()
		shaixuan(self.driver).typeqk(-100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()
		shaixuan(self.driver).clickkehu()
		shaixuan(self.driver).clickshaixuan()

		#筛选
		#分组先跳过
		
		#负责人：
		shaixuan(self.driver).sx_fuzeren()
		shaixuan(self.driver).sx_laoban()
		shaixuan(self.driver).sx_queding()
		

		sleep(5)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



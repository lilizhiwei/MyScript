from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("./page")
from page.page_daoru import login

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#导入正确
		login(self.driver).user_login()
		login(self.driver).clickqingkong()
		login(self.driver).bccg()
		login(self.driver).clickkehu()
		login(self.driver).clickX()
		login(self.driver).clickdaoru()
		login(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lq.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'20')
		self.assertEqual(login(self.driver).cuo(),'0')

		#导入错误
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\le.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'10')
		self.assertEqual(login(self.driver).cuo(),'10')

		#导入大量
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lw.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'1774')
		self.assertEqual(login(self.driver).cuo(),'0')

	def test_2gonghuoshang(self):
		#导入正确
		login(self.driver).user_login()
		login(self.driver).clickghs()
		login(self.driver).clickX()
		login(self.driver).clickdaoru2()
		login(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lq.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'20')
		self.assertEqual(login(self.driver).cuo(),'0')

		#导入错误
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\le.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'10')
		self.assertEqual(login(self.driver).cuo(),'10')

		#导入大量
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lw.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'1774')
		self.assertEqual(login(self.driver).cuo(),'0')

	def test_3shangpin(self):
		# 导入正确
		login(self.driver).user_login()
		login(self.driver).clicksp()
		login(self.driver).clickX()
		login(self.driver).clickdaoru3()
		login(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\sq.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'20')
		self.assertEqual(login(self.driver).cuo(),'0')

		#导入错误
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\se.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'10')
		self.assertEqual(login(self.driver).cuo(),'10')

		#导入大量
		login(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\sw.exe")
		login(self.driver).clicktijiao()
		login(self.driver).yanzheng()
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickque()
		self.assertEqual(login(self.driver).dui(),'983')
		self.assertEqual(login(self.driver).cuo(),'30')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



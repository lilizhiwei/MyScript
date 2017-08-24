from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.pc_daoru import daoru

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#导入正确
		daoru(self.driver).user_login()
		daoru(self.driver).clickqingkong()
		daoru(self.driver).bccg()
		daoru(self.driver).clickkehu()
		daoru(self.driver).clickX()
		daoru(self.driver).clickdaoru()
		daoru(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lq.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'20')
		self.assertEqual(daoru(self.driver).cuo(),'0')

		#导入错误
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\le.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'10')
		self.assertEqual(daoru(self.driver).cuo(),'10')

		#导入大量
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lw.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'1774')
		self.assertEqual(daoru(self.driver).cuo(),'0')

	def test_2gonghuoshang(self):
		#导入正确
		daoru(self.driver).user_login()
		daoru(self.driver).clickghs()
		daoru(self.driver).clickX()
		daoru(self.driver).clickdaoru2()
		daoru(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lq.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'20')
		self.assertEqual(daoru(self.driver).cuo(),'0')

		#导入错误
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\le.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'10')
		self.assertEqual(daoru(self.driver).cuo(),'10')

		#导入大量
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lw.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'1774')
		self.assertEqual(daoru(self.driver).cuo(),'0')

	def test_3shangpin(self):
		# 导入正确
		daoru(self.driver).user_login()
		daoru(self.driver).clicksp()
		daoru(self.driver).clickX()
		daoru(self.driver).clickdaoru3()
		daoru(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\sq.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'20')
		self.assertEqual(daoru(self.driver).cuo(),'0')

		#导入错误
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\se.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'10')
		self.assertEqual(daoru(self.driver).cuo(),'10')

		#导入大量
		daoru(self.driver).clickshang2()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\sw.exe")
		daoru(self.driver).clicktijiao()
		daoru(self.driver).yanzheng()
		self.assertEqual(daoru(self.driver).clickwanbi(),'导入完毕')
		daoru(self.driver).clickque()
		self.assertEqual(daoru(self.driver).dui(),'983')
		self.assertEqual(daoru(self.driver).cuo(),'30')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



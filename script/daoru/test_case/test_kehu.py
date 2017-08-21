from selenium import webdriver
from time import sleep
import unittest,sys
sys.path.append("./page")
from page.page_daoru import login

class loginTest(unittest.TestCase):
	'''社区登录测试'''

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()

	def test1(self):
		login(self.driver).user_login()
		login(self.driver).clickkehu()
		login(self.driver).clickX()
		login(self.driver).clickdaoru()
		sleep(4)
		login(self.driver).clickshang()
		sleep(1)
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\lianzheng.exe")
		sleep(1)
		login(self.driver).clicktijiao()
		sleep(5)
		self.assertEqual(login(self.driver).clickwanbi(),'导入完毕')
		login(self.driver).clickqueding()
		sleep(5)










	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



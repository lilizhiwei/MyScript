from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_spyw import spyw
from page_obj.pc_daoru import daoru

class loginTest(unittest.TestCase):
	'''批量导入功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1daoru(self):
		#修改权限
		daoru(self.driver).user_login_xh()
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).sp_daoru()
		spyw(self.driver).clickbc()

		#验证1
		daoru(self.driver).clicksp()
		daoru(self.driver).clickX()
		daoru(self.driver).clickdaoru3()
		daoru(self.driver).clickshang()
		os.system("C:\\Users\\Administrator\\MyScript\\excel\\sq.exe")
		daoru(self.driver).clicktijiao()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content"),"权限不足"))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content").text,'权限不足')
		self.driver.find_element_by_link_text("确定").click()

	def test_2shanchu(self):
		daoru(self.driver).user_login_xh()

		#验证1
		daoru(self.driver).clicksp()
		daoru(self.driver).clickX()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='147']")))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_xpath("//*[@data-power='147']").get_attribute("class"),"hide")

		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).sp_daoru()
		spyw(self.driver).sp_shanchu()
		spyw(self.driver).clickbc()

		#验证2

	def test_3xiugai(self):
		daoru(self.driver).user_login_xh()

		#验证2




		#修改权限
		spyw(self.driver).clickyg()
		spyw(self.driver).clickqx()
		spyw(self.driver).clickspyw()
		spyw(self.driver).sp_shanchu()
		# spyw(self.driver).sp_xiugai()
		spyw(self.driver).clickbc()

		#验证3



	
	# def test_4xinzeng(self):
	
	# def test_5chakan(self):
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



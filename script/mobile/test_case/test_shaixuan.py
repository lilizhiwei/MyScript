from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest,sys,os,random,re
sys.path.append("../../page_obj")
from page_obj.mobile_lianxiren import shaixuan

class loginTest(unittest.TestCase):
	'''筛选功能测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kehu(self):
		#创建一个有分组，负责人营业员，有欠款
		shaixuan(self.driver).user_login()
		shaixuan(self.driver).openmobile()
		shaixuan(self.driver).clicklianxiren()
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fenzu()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser(name1)
		fz = str(a) + '分组' + str(b)
		shaixuan(self.driver).clickfenzu(fz)
		shaixuan(self.driver).clickfuzeren()
		shaixuan(self.driver).typeqk(100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#创建一个无分组，有预存
		shaixuan(self.driver).xzkh()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser(name2)
		shaixuan(self.driver).typeqk(-100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#筛选
		#分组
		#shaixuan(self.driver).clickkehu()
		#shaixuan(self.driver).clickshaixuan()
		#WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='%s']" % fz),fz))
		#sleep(0.5)
		#self.driver.find_element_by_xpath("//*[text()='%s']" % fz).click()
		#shaixuan(self.driver).sx_queding()
		#WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		#self.assertIn(name1,shaixuan(self.driver).yz_kehu())
		
		#负责人：
		shaixuan(self.driver).clickkehu()
		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).sx_fuzeren()
		shaixuan(self.driver).sx_yingyeyuan()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())

		#状态
		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).sx_zt()
		shaixuan(self.driver).sx_qk()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())

		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).clickqk()
		shaixuan(self.driver).sx_zt()
		shaixuan(self.driver).sx_qk()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())
		self.assertRegexpMatches(shaixuan(self.driver).yz_kehu()，r'*')

	def test_2ghs(self):
		#创建一个有分组，负责人营业员，有欠款
		shaixuan(self.driver).user_login()
		shaixuan(self.driver).openmobile()
		shaixuan(self.driver).clicklianxiren()
		shaixuan(self.driver).xzghs()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).fenzu()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).fuzeren()
		shaixuan(self.driver).tjgdx1()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser1(name1)
		fz = str(a) + '分组' + str(b)
		shaixuan(self.driver).clickfenzu(fz)
		shaixuan(self.driver).clickfuzeren()
		shaixuan(self.driver).typeqk(100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#创建一个无分组，有预存
		shaixuan(self.driver).xzghs()
		shaixuan(self.driver).tjgdx()
		shaixuan(self.driver).dqqk()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '李志伟' + str(b)
		shaixuan(self.driver).typeuser1(name2)
		shaixuan(self.driver).typeqk(-100)
		shaixuan(self.driver).baocun()
		shaixuan(self.driver).bccg1()

		#筛选
		#分组
		#shaixuan(self.driver).clickkehu()
		#shaixuan(self.driver).clickshaixuan()
		#WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='%s']" % fz),fz))
		#sleep(0.5)
		#self.driver.find_element_by_xpath("//*[text()='%s']" % fz).click()
		#shaixuan(self.driver).sx_queding()
		#WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		#self.assertIn(name1,shaixuan(self.driver).yz_kehu())
		
		#负责人：
		shaixuan(self.driver).clickghs()
		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).sx_fuzeren()
		shaixuan(self.driver).sx_yingyeyuan()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())

		#状态
		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).sx_zt()
		shaixuan(self.driver).sx_qk()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())

		shaixuan(self.driver).clickshaixuan()
		shaixuan(self.driver).clickqk()
		shaixuan(self.driver).sx_zt()
		shaixuan(self.driver).sx_qk()
		shaixuan(self.driver).sx_queding()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".media-heading"),name1))
		self.assertIn(name1,shaixuan(self.driver).yz_kehu())

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



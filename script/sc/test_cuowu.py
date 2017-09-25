from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os,random
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class scLJ(unittest.TestCase):
	'''商城-拦截测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_cw(self):

		#验证错误拦截项
		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		bh1 = str(a) + str(b)
		sc(self.driver).cj_kh(name1,bh1)
		name2 = str(a) + '商品1' + str(b)
		sc(self.driver).cj_sp1(name2)
		self.driver.find_element_by_css_selector('.lcs_cursor').click()

		#登录项
		sc(self.driver).loginsc1()
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"您需要填写账号名称"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*您需要填写账号名称[\s\S]*")
		self.driver.find_element_by_css_selector(".uName").send_keys(12345)
		self.driver.find_element_by_css_selector(".uPass").send_keys(123456)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"未注册帐号"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*未注册帐号[\s\S]*")
		self.driver.find_element_by_css_selector(".uName").clear()
		self.driver.find_element_by_css_selector(".uPass").clear()
		self.driver.find_element_by_css_selector(".uName").send_keys(bh1)
		self.driver.find_element_by_css_selector(".uPass").send_keys(1234)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"密码错误"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*密码错误[\s\S]*")
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@class="button button-big button-round unLogin"]')))
		sleep(2)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-round unLogin"]').click()

		#下单项
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"1"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"您还没填写您的收货联系人"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*您还没填写您的收货联系人[\s\S]*")
		self.driver.find_element_by_xpath('//*[text()="确定"]').click()
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人姓名"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人姓名"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="联系人姓名"]').send_keys("李志伟")
		self.driver.find_element_by_css_selector('.content-block>a').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.col-30>div')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"您还没填写您的收货联系方式"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*您还没填写您的收货联系方式[\s\S]*")


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



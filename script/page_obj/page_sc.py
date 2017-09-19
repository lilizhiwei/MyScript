from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class sc(page):
	def opensc(self):
		self.driver.get('http://lilizhiwei.yyddd.com/login.html')

	def loginsc(self,name):
		self.driver.get('http://lilizhiwei.yyddd.com/')
		self.opensc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".uName")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".uName").send_keys(name)
		self.driver.find_element_by_css_selector(".uPass").send_keys(123456)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".tab-label"),"商城"))
		sleep(0.5)

	def tj_sp1(self):
		self.driver.find_element_by_xpath('//ul/li//div[@class="item-title"]').click()
	
	def tj_sp2(self):
		self.driver.find_element_by_xpath('//ul/li[2]//div[@class="item-title"]').click()
	
	def tj_sp3(self):
		self.driver.find_element_by_xpath('//ul/li[3]//div[@class="item-title"]').click()
	
	def jr_gwc(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='加入购物车']"),"加入购物车"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='加入购物车']").click()
		sleep(0.5)
	
	def clickdw(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='箱(10个)']"),"箱(10个)"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='箱(10个)']").click()
	
	def clickgwc(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='购物车']"),"购物车"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='购物车']").click()

	def clicksc(self):
		self.driver.find_element_by_xpath('//ul/li[3]//i[@class="icon icon-remove"]').click()
		self.driver.find_element_by_css_selector('.modal-button.modal-button-bold').click()

	def shdz1(self):
		self.driver.find_element_by_xpath("//*[text()='我']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//ul/li[2]//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li[2]//i").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人手机/固话"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').send_keys(13140023070)
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').send_keys('河南郑州')
		self.driver.find_element_by_css_selector('.content-block>a').click()

	def shdz2(self):
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人手机/固话"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').send_keys(13523148316)
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').send_keys('河南商丘')
		self.driver.find_element_by_css_selector('.content-block>a').click()

	def sc_dd(self):
		self.driver.find_element_by_xpath("//*[text()='我']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//ul/li//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li//i").click()

	def clicktj(self):
		self.driver.find_element_by_css_selector('.col-30>div').click()
	
	def liuyan(self):
		self.driver.find_element_by_css_selector('.setRem').send_keys("尽快送货")
	
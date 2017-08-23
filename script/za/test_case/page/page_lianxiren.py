from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import unittest

class login(object):
	'''用户登录页面'''

	username = '13140023070'
	password = '123456'

	def __init__(self, selenium_driver,user=username,pwd=password):
		self.user = user
		self.pwd = pwd
		self.driver = selenium_driver
		self.timeout = 30

	#打开网址
	def openpc(self):
		self.driver.get('http://www.yyddd.com/pc/login.html')
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
	
	def openmobile(self):
		self.driver.get('http://www.yyddd.com/mobile')

	#统一登录
	def user_login(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span.remember"),"老板"))
		sleep(0.5)
		self.openmobile()

	def clicklianxiren(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.LINK_TEXT,"联系人"),"联系人"))
		sleep(0.5)
		self.driver.find_element_by_link_text("联系人").click()

	def xzkh(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//li[@data-power='162']//h5"),"新增客户"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//li[@data-power='162']").click()

	def tjgdx(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.text-center.padding-vertical-15"),"添加更多项"))
		sleep(0.5)
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def tjgdx1(self):
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def fenzu(self):
		self.driver.find_element_by_xpath("//li[@data-role='group']").click()

	def dqqk(self):
		self.driver.find_element_by_xpath("//li[@data-role='begin']").click()

	def fuzeren(self):
		self.driver.find_element_by_xpath("//li[@data-role='staff']").click()

	def typeuser(self):
		name = 'lilizhiwei'
		self.driver.find_element_by_xpath("//input[@placeholder='客户名称']").send_keys(name)

	def typeqk(self,qk):
		self.driver.find_element_by_xpath("//div[@data-append='begin']//input").send_keys(qk)




	






































	
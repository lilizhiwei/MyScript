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
		self.opensc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".uName")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".uName").send_keys(name)
		self.driver.find_element_by_css_selector(".uPass").send_keys(123456)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".tab-label"),"商城"))
		sleep(0.5)

	def click(self):
		pass
	
	def click(self):
		pass
	
	def click(self):
		pass
	
	def click(self):
		pass
	
	def click(self):
		pass
	
	def click(self):
		pass
	
	
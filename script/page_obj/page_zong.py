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
	
	#统一登录
	def user_login(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()


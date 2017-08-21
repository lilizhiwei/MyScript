from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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

	#填写账号
	def login_username(self):
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)

	#填写密码
	def login_password(self):
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)

	#点击登录按钮
	def login_button(self):
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
	
	#统一登录
	def user_login(self):
		self.openpc()
		self.login_username()
		self.login_password()
		self.login_button()
		sleep(1)

	#进入客户页面
	def clickkehu(self):
		self.driver.find_element_by_link_text("客户").click()

	def clickX(self):
		self.driver.find_element_by_xpath("//button[@data-toggle='dropdown']/i").click()

	def clickdaoru(self):
		self.driver.find_element_by_xpath("//li[@data-power='167']//i").click()

	def clickshang(self):
		self.driver.find_element_by_css_selector("p:contains('上传数据文件模板')>button").click()

	def clicktijiao(self):
		self.driver.find_element_by_css_selector(".fa.fa-check.fa-fw").click()

	def clickwanbi(self):
		return self.driver.find_element_by_css_selector(".layui-layer-content").text

	def clickqueding(self):
		self.driver.find_element_by_link_text("确定").click()










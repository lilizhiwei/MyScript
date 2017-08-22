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
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
	
	#统一登录
	def user_login(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
		sleep(1)

	#清空数据
	def clickqingkong(self):
		self.driver.find_element_by_xpath("//i[@class='site-menu-icon fa fa-cog']").click()
		self.driver.find_element_by_link_text("通用设置").click()
		sleep(1)
		self.driver.find_element_by_css_selector("span.padding-left-5").click()
		sleep(2)
		self.driver.find_element_by_xpath("//div/div/div[2]/div/button").click()
		self.driver.find_element_by_xpath("//div[2]/div/button[2]").click()
		self.driver.find_element_by_css_selector("input.layui-layer-input").send_keys(self.pwd)
		self.driver.find_element_by_css_selector("a.layui-layer-btn0.pull-right").click()
		sleep(3)

	#进入客户页面
	def clickkehu(self):
		self.driver.find_element_by_xpath("//i[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("客户").click()

	def clickghs(self):
		self.driver.find_element_by_xpath("//i[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("供货商").click()

	def clicksp(self):
		self.driver.find_element_by_xpath("//i[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("商品库存").click()

	def clickX(self):
		self.driver.find_element_by_xpath("//i[@class='icon fa fa-file-excel-o']").click()

	def clickdaoru(self):
		self.driver.find_element_by_xpath("//li[@data-power='167']//i").click()

	def clickdaoru2(self):
		self.driver.find_element_by_xpath("//li[@data-power='176']//i").click()

	def clickdaoru3(self):
		self.driver.find_element_by_xpath("//li[@data-power='147']//i").click()

	def clickshang(self):
		self.driver.find_element_by_xpath("//i[@class='fa fa-cloud-upload fa-4x fa-fw']").click()

	def clickshang2(self):
		self.driver.find_element_by_xpath("//i[@class='fa fa-refresh fa-4x fa-fw']").click()

	def clicktijiao(self):
		self.driver.find_element_by_css_selector("i.fa.fa-check.fa-fw").click()

	def clickwanbi(self):
		return self.driver.find_element_by_css_selector("div.layui-layer-content").text

	def clickque(self):
		self.driver.find_element_by_link_text("确定").click()

	def dui(self):
		return self.driver.find_element_by_css_selector(".datasuccesslength").text

	def cuo(self):
		return self.driver.find_element_by_css_selector(".dataerrorlength").text

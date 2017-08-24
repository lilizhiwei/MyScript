from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import unittest

class page(object):
	'''用户登录页面'''

	username = '13140023070'
	password = '123456'

	def __init__(self, driver,user=username,pwd=password):
		self.user = user
		self.pwd = pwd
		self.driver = driver
		self.timeout = 30

	#打开网址
	def openpc(self):
		self.driver.get('http://www.yyddd.com/pc/login.html')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def openmobile(self):
		self.driver.get('http://www.yyddd.com/mobile')

	
	#统一登录
	def user_login(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//*[@type='submit']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".remember"),"老板"))
		sleep(0.5)

	#清空数据
	def clickqingkong(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cog']").click()
		self.driver.find_element_by_link_text("通用设置").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".padding-left-5")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".padding-left-5").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//div/div/div[2]/div/button")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//div/div/div[2]/div/button").click()
		self.driver.find_element_by_xpath("//div[2]/div/button[2]").click()
		self.driver.find_element_by_css_selector(".layui-layer-input").send_keys(self.pwd)
		self.driver.find_element_by_css_selector(".layui-layer-btn0.pull-right").click()

	#pc端保存成功
	def bccg(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"保存成功！"))
		sleep(0.5)
	
	#移动端保存成功
	def bccg1(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handler='ok']"),"确定"))
		self.driver.find_element_by_xpath("//*[@data-handler='ok']").click()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest,random

class shaixuan(page):

	def clicklianxiren(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.LINK_TEXT,"联系人"),"联系人"))
		sleep(0.5)
		self.driver.find_element_by_link_text("联系人").click()

	def xzkh(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-power='162']//h5"),"新增客户"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='162']").click()

	def tjgdx(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.text-center.padding-vertical-15"),"添加更多项"))
		sleep(0.5)
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def tjgdx1(self):
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def fenzu(self):
		self.driver.find_element_by_xpath("//*[@data-role='group']").click()

	def dqqk(self):
		self.driver.find_element_by_xpath("//*[@data-role='begin']").click()

	def fuzeren(self):
		self.driver.find_element_by_xpath("//*[@data-role='staff']").click()

	def typeuser(self):
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		c = str(a) + '李志伟' + str(b)
		self.driver.find_element_by_xpath("//*[@placeholder='客户名称']").send_keys(c)

	def typeqk(self,qk):
		self.driver.find_element_by_xpath("//*[@data-append='begin']//input").send_keys(qk)

	def baocun(self):
		self.driver.find_element_by_xpath("//*[@data-action='save']").click()

	def clickfenzu(self):
		self.driver.find_element_by_xpath("//*[@data-plugin='group']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handle='add']"),"新增"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-handle='add']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handler='save']"),"确认"))
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		c = str(a) + '分组' + str(b)
		self.driver.find_element_by_xpath("//*[@placeholder='填写分组']").send_keys(c)
		self.driver.find_element_by_xpath("//*[@data-handler='save']").click()

	def clickfuzeren(self):
		self.driver.find_element_by_xpath("//*[@data-plugin='staff']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='营业员']"),"营业员"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='营业员']").click()


	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	def fz(self):
		pass

	
	






































	
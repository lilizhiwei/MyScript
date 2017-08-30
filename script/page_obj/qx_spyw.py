from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class spyw(page):

	#进入页面
	def clickspyw(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='goods']").click()

	def clickquanxuan_spgl(self):
		self.driver.find_element_by_xpath("//div/span[text()='商品管理']/../button").click()

	def clickquanxuan_jhd(self):
		self.driver.find_element_by_xpath("//div/span[text()='采购单']/../button").click()
	
	def clickquanxuan_xhd(self):
		self.driver.find_element_by_xpath("//div/span[text()='销售单']/../button").click()
		
	def sp_chakan(self):
		self.driver.find_element_by_id("141").click()

	def sp_xinzeng(self):
		self.driver.find_element_by_id("142").click()

	def sp_xiugai(self):
		self.driver.find_element_by_id("143").click()

	def sp_shanchu(self):
		self.driver.find_element_by_id("144").click()

	def sp_daoru(self):
		self.driver.find_element_by_id("147").click()

	def jh_chakan(self):
		self.driver.find_element_by_id("121").click()

	def jh_xinzeng(self):
		self.driver.find_element_by_id("122").click()

	def jh_xiugai(self):
		self.driver.find_element_by_id("123").click()

	def jh_shanchu(self):
		self.driver.find_element_by_id("124").click()

	def xs_chakan(self):
		self.driver.find_element_by_id("101").click()

	def xs_xinzeng(self):
		self.driver.find_element_by_id("102").click()

	def xs_xiugai(self):
		self.driver.find_element_by_id("103").click()

	def xs_shanchu(self):
		self.driver.find_element_by_id("104").click()
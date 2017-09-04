from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class gjqx(page):

	#进入页面
	def clickgjqx(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='super']").click()

	def clickquanxuan_yg(self):
		self.driver.find_element_by_xpath("//div/span[text()='员工管理']/../button").click()

	def clickquanxuan_qt(self):
		self.driver.find_element_by_xpath("//div/span[text()='其他']/../button").click()

	def yg_chakan(self):
		self.driver.find_element_by_id("400").click()

	def yg_xinzeng(self):
		self.driver.find_element_by_id("401").click()

	def yg_xiugai(self):
		self.driver.find_element_by_id("402").click()

	def yg_shanchu(self):
		self.driver.find_element_by_id("403").click()

	def yg_tingyong(self):
		self.driver.find_element_by_id("404").click()

	def yg_mima(self):
		self.driver.find_element_by_id("405").click()
	
	def qt_bianji(self):
		self.driver.find_element_by_id("412").click()
	
	def qt_rizhi(self):
		self.driver.find_element_by_id("420").click()
	
	def qt_jishi(self):
		self.driver.find_element_by_id("432").click()
	
	def qt_zhiwei(self):
		self.driver.find_element_by_id("403").click()

	def qt_jiaojie(self):
		self.driver.find_element_by_id("421").click()
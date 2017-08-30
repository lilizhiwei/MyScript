from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class wldw(page):

	#进入页面
	def clickwldw(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='contacts']").click()

	def clickquanxuan(self):
		self.driver.find_element_by_xpath("//div/span[text()='客户']/../button").click()

	def qx_jifen(self):
		self.driver.find_element_by_id("169").click()

	def qx_gongxiang(self):
		self.driver.find_element_by_id("168").click()

	def qx_daoru(self):
		self.driver.find_element_by_id("167").click()

	def qx_shanchu(self):
		self.driver.find_element_by_id("164").click()

	def qx_xiugai(self):
		self.driver.find_element_by_id("163").click()

	def qx_xinzeng(self):
		self.driver.find_element_by_id("162").click()

	def qx_chakan(self):
		self.driver.find_element_by_id("161").click()

	def clickquanxuan_ghs(self):
		self.driver.find_element_by_xpath("//div/span[text()='供应商']/../button").click()

	def qx_ghs_gongxiang(self):
		self.driver.find_element_by_id("178").click()

	def qx_ghs_daoru(self):
		self.driver.find_element_by_id("176").click()

	def qx_ghs_shanchu(self):
		self.driver.find_element_by_id("173").click()

	def qx_ghs_xiugai(self):
		self.driver.find_element_by_id("172").click()

	def qx_ghs_xinzeng(self):
		self.driver.find_element_by_id("171").click()

	def qx_ghs_chakan(self):
		self.driver.find_element_by_id("170").click()


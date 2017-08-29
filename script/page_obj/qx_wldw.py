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

	

	def clickkehu(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("客户").click()

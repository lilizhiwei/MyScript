from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class cwgl(page):

	#进入页面
	def clickwldw(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='contacts']").click()

	def clickquanxuan(self):
		self.driver.find_element_by_xpath("//div/span[text()='客户']/../button").click()

	def qx_jifen(self):
		self.driver.find_element_by_id("169").click()
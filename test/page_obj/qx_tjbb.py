from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class tjbb(page):

	#进入页面
	def clicktjbb(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='analysis']").click()

	def clickquanxuan_xs(self):
		self.driver.find_element_by_xpath("//div/span[text()='销售报表']/../button").click()

	def clickquanxuan_jh(self):
		self.driver.find_element_by_xpath("//div/span[text()='进货报表']/../button").click()

	def clickquanxuan_kc(self):
		self.driver.find_element_by_xpath("//div/span[text()='库存分析报表']/../button").click()

	def clickquanxuan_ys(self):
		self.driver.find_element_by_xpath("//div/span[text()='应收/储值报表']/../button").click()

	def clickquanxuan_yf(self):
		self.driver.find_element_by_xpath("//div/span[text()='应付款报表']/../button").click()

	def clickquanxuan_sz(self):
		self.driver.find_element_by_xpath("//div/span[text()='收支报表']/../button").click()

	def xs_chakan(self):
		self.driver.find_element_by_id("320").click()

	def xs_mingxi(self):
		self.driver.find_element_by_id("321").click()

	def lr_chakan(self):
		self.driver.find_element_by_id("310").click()

	def lr_mingxi(self):
		self.driver.find_element_by_id("311").click()

	def jh_chakan(self):
		self.driver.find_element_by_id("330").click()

	def jh_mingxi(self):
		self.driver.find_element_by_id("331").click()

	def kc_chakan(self):
		self.driver.find_element_by_id("340").click()

	def kc_mingxi(self):
		self.driver.find_element_by_id("341").click()

	def ys_chakan(self):
		self.driver.find_element_by_id("350").click()

	def ys_mingxi(self):
		self.driver.find_element_by_id("351").click()

	def yf_chakan(self):
		self.driver.find_element_by_id("360").click()

	def yf_mingxi(self):
		self.driver.find_element_by_id("361").click()

	def sz_chakan(self):
		self.driver.find_element_by_id("370").click()

	def sz_mingxi(self):
		self.driver.find_element_by_id("371").click()

	
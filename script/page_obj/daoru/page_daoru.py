from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import unittest

class daoru(object):
	'''用户登录页面'''

	password = '123456'

	def __init__(self, selenium_driver,user=username,pwd=password):
		self.pwd = pwd
		self.driver = selenium_driver
		self.timeout = 30

	#清空数据
	def clickqingkong(self):
		self.driver.find_element_by_xpath("//i[@class='site-menu-icon fa fa-cog']").click()
		self.driver.find_element_by_link_text("通用设置").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.padding-left-5")))
		sleep(0.5)
		self.driver.find_element_by_css_selector("span.padding-left-5").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//div/div/div[2]/div/button")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//div/div/div[2]/div/button").click()
		self.driver.find_element_by_xpath("//div[2]/div/button[2]").click()
		self.driver.find_element_by_css_selector("input.layui-layer-input").send_keys(self.pwd)
		self.driver.find_element_by_css_selector("a.layui-layer-btn0.pull-right").click()

	def bccg(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"保存成功！"))
		sleep(0.5)

	#进入页面
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
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='fa fa-cloud-upload fa-4x fa-fw']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//i[@class='fa fa-cloud-upload fa-4x fa-fw']").click()

	def clickshang2(self):
		self.driver.find_element_by_xpath("//i[@class='fa fa-refresh fa-4x fa-fw']").click()

	def clicktijiao(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".btn.btn-primary.margin-top-15.sender"),"确认提交"))
		sleep(0.5)
		self.driver.find_element_by_css_selector("i.fa.fa-check.fa-fw").click()

	def yanzheng(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.layui-layer-content"),"导入完毕"))

	def clickwanbi(self):
		return self.driver.find_element_by_css_selector("div.layui-layer-content").text

	def clickque(self):
		self.driver.find_element_by_link_text("确定").click()

	def dui(self):
		return self.driver.find_element_by_css_selector(".datasuccesslength").text

	def cuo(self):
		return self.driver.find_element_by_css_selector(".dataerrorlength").text

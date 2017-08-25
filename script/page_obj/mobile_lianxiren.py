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

	def xzghs(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-power='171']//h5"),"新增供货商"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='171']").click()

	def tjgdx(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div.text-center.padding-vertical-15"),"添加更多项"))
		sleep(0.5)
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def tjgdx1(self):
		self.driver.find_element_by_css_selector("div.text-center.padding-vertical-15").click()

	def fenzu(self):
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-role='group']").click()

	def dqqk(self):
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-role='begin']").click()

	def fuzeren(self):
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-role='staff']").click()

	def typeuser(self,name):
		self.driver.find_element_by_xpath("//*[@placeholder='客户名称']").send_keys(name)

	def typeuser1(self,name):
		self.driver.find_element_by_xpath("//*[@placeholder='供应商名称']").send_keys(name)

	def typeqk(self,qk):
		self.driver.find_element_by_xpath("//*[@data-append='begin']//input").send_keys(qk)

	def baocun(self):
		self.driver.find_element_by_xpath("//*[@data-action='save']").click()

	def clickfenzu(self,fz):
		self.driver.find_element_by_xpath("//*[@data-plugin='group']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handle='add']"),"新增"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-handle='add']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handler='save']"),"确认"))
		self.driver.find_element_by_xpath("//*[@placeholder='填写分组']").send_keys(fz)
		self.driver.find_element_by_xpath("//*[@data-handler='save']").click()

	def clickfuzeren(self):
		self.driver.find_element_by_xpath("//*[@data-plugin='staff']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='营业员']"),"营业员"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='营业员']").click()

	def clickkehu(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-power='161']//h5"),"客户"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='161']").click()

	def clickghs(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-power='170']//h5"),"供货商"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='170']").click()

	def clickshaixuan(self):
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".fa.fa-filter")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".fa.fa-filter").click()

	def sx_fuzeren(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='负责人']"),"负责人"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='负责人']").click()

	def sx_yingyeyuan(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='营业员']"),"营业员"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='营业员']").click()

	def sx_queding(self):
		self.driver.find_element_by_xpath("//*[@data-handle='sure']").click()

	def yz_kehu(self):
		return self.driver.find_element_by_css_selector(".media-heading").text

	def sx_zt(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='状态']"),"状态"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='状态']").click()
	
	def sx_qk(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='有欠款']"),"有欠款"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='有欠款']").click()

	def clickqk(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='清空已选']"),"清空已选"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='清空已选']").click()
		sleep(1)






































	
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest,random

class sc(page):
	def opensc(self):
		self.driver.get('http://lilizhiwei.yyddd.com/')
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".tab-label"),"商城"))
		sleep(0.5)

	def loginsc(self,name):
		self.opensc()
		self.driver.get('http://lilizhiwei.yyddd.com/login.html')
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".uName")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".uName").send_keys(name)
		self.driver.find_element_by_css_selector(".uPass").send_keys(123456)
		self.driver.find_element_by_xpath('//*[@class="button button-big button-fill login"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".tab-label"),"商城"))
		sleep(0.5)

	def tj_sp1(self):
		self.driver.find_element_by_xpath('//ul/li//div[@class="item-title"]').click()
	
	def tj_sp2(self):
		self.driver.find_element_by_xpath('//ul/li[2]//div[@class="item-title"]').click()
	
	def tj_sp3(self):
		self.driver.find_element_by_xpath('//ul/li[3]//div[@class="item-title"]').click()
	
	def jr_gwc(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='加入购物车']"),"加入购物车"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='加入购物车']").click()
		sleep(0.5)
	
	def clickdw(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='箱(10个)']"),"箱(10个)"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='箱(10个)']").click()
	
	def clickgwc(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='购物车']"),"购物车"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='购物车']").click()

	def clicksc(self):
		self.driver.find_element_by_xpath('//ul/li[3]//i[@class="icon icon-remove"]').click()
		self.driver.find_element_by_css_selector('.modal-button.modal-button-bold').click()

	def shdz1(self):
		self.driver.find_element_by_xpath("//*[text()='我']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//ul/li[2]//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li[2]//i").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人手机/固话"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').send_keys(13140023070)
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').send_keys('河南郑州')
		self.driver.find_element_by_css_selector('.content-block>a').click()

	def shdz2(self):
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人手机/固话"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').send_keys(13523148316)
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').send_keys('河南商丘')
		self.driver.find_element_by_css_selector('.content-block>a').click()

	def shdz3(self):
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="联系人手机/固话"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="联系人手机/固话"]').send_keys(13523148316)
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="详细地址"]').send_keys('河南商丘')
		self.driver.find_element_by_xpath('//*[@placeholder="联系人姓名"]').clear()
		self.driver.find_element_by_xpath('//*[@placeholder="联系人姓名"]').send_keys("李志伟")
		self.driver.find_element_by_css_selector('.content-block>a').click()

	def sc_dd(self):
		self.driver.find_element_by_xpath("//*[text()='我']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//ul/li//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//ul/li//i").click()

	def clicktj(self):
		self.driver.find_element_by_css_selector('.col-30>div').click()
	
	def liuyan(self):
		self.driver.find_element_by_css_selector('.setRem').send_keys("尽快送货")

	def cj_kh(self,name1,bh1):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("新增客户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="cname"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-role="cname"]').send_keys(name1)
		self.driver.find_element_by_xpath('//*[@data-option="bh"]//input').send_keys(bh1)
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-option="upwd"]//input')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-option="upwd"]//input').send_keys(123456)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

	def cj_sp1(self,name2):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("商品库存").click()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增商品").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-role="gname"]').send_keys(name2)
		self.driver.find_element_by_xpath('//*[@data-role="sellprice"]').send_keys(20)
		self.driver.find_element_by_link_text("库存信息").click()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').clear()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').send_keys(50)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

	def cj_sp2(self,name3):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增商品").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-role="gname"]').send_keys(name3)
		self.driver.find_element_by_xpath('//*[@data-role="sellprice"]').send_keys(20)
		self.driver.find_element_by_xpath('//*[@data-role="gunit"]').click()
		self.driver.find_element_by_xpath("//*[text()='个']").click()
		self.driver.find_element_by_xpath('//*[@data-role="gunit2"]').click()
		self.driver.find_element_by_xpath("//div[@id='exampleTabsLineOne']/div/div[2]/div[5]/div/div/span/div/div/div[2]").click()
		self.driver.find_element_by_xpath('//*[@data-role="transNum"]').send_keys(10)
		self.driver.find_element_by_link_text("库存信息").click()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').clear()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').send_keys(50)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

	def cj_sp3(self,name3,fl1,fl2):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增商品").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-role="gname"]').send_keys(name3)
		self.driver.find_element_by_xpath('//*[@data-role="sellprice"]').send_keys(20)
		self.driver.find_element_by_css_selector(".fa.fa-pencil.fa-fw").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-gg-action="add"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-gg-action="add"]').click()
		self.driver.find_element_by_css_selector('.layui-layer-input').send_keys(fl1)
		self.driver.find_element_by_link_text('确定').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@data-gg-action="addsub"]').click()
		self.driver.find_element_by_css_selector('.layui-layer-input').send_keys(fl2)
		self.driver.find_element_by_link_text('确定').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@data-gg-action="close"]').click()
		self.driver.find_element_by_xpath('//*[@class="btn dropdown-toggle bs-placeholder btn-default"]').send_keys(Keys.SPACE)
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,fl2)))
		sleep(0.5)
		self.driver.find_element_by_link_text(fl2).click()
		self.driver.find_element_by_xpath('//*[@data-role="gattribute"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-gg-action="editModle"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-gg-action="editModle"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-gg-action="add"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-gg-action="add"]').click()
		self.driver.find_element_by_css_selector('.layui-layer-input').send_keys("品牌")
		self.driver.find_element_by_link_text('确定').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@data-gg-action="addsub"]').click()
		self.driver.find_element_by_css_selector('.layui-layer-input').send_keys("iphone")
		self.driver.find_element_by_link_text('确定').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@data-gg-action="editModle"]').click()
		sleep(1)
		self.driver.find_element_by_xpath('//li[@data-gg-action="choose"]').click()1
		sleep(1)
		self.driver.find_element_by_xpath('//button[@data-gg-action="sure"]').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@data-role="gunit"]').click()
		self.driver.find_element_by_xpath("//*[text()='个']").click()
		self.driver.find_element_by_xpath('//*[@data-role="gunit2"]').click()
		self.driver.find_element_by_xpath("//div[@id='exampleTabsLineOne']/div/div[2]/div[5]/div/div/span/div/div/div[2]").click()
		self.driver.find_element_by_xpath('//*[@data-role="transNum"]').send_keys(10)
		self.driver.find_element_by_link_text("库存信息").click()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').clear()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').send_keys(50)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

	def cj_tc(self,name4):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增套餐").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-role="gname"]').send_keys(name4)
		self.driver.find_element_by_xpath('//*[@data-role="sellprice"]').send_keys(20)
		self.driver.find_element_by_xpath('//*[@data-action="addgoods"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//tr/td[8]/div/div/span[2]/i')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//tr/td[8]/div/div/span[2]/i').click()
		self.driver.find_element_by_xpath('//tr[2]/td[8]/div/div/span[2]/i').click()
		sleep(0.5)
		self.driver.find_element_by_link_text("确定").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

	def sp_sj(self,name4):
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		self.driver.find_element_by_xpath('//tr[2]//div[@class="lcs_cursor"]').click()
		sleep(1)
		self.driver.find_element_by_xpath("//a[2]/span/span/small").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.title'),name4))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		sleep(1)

	def ty_ss(self,name):
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.ID,"search")))
		sleep(0.5)
		self.driver.find_element_by_id('search').send_keys(name)
		self.driver.find_element_by_id('search').send_keys(Keys.SPACE)

	def sp_sx(self,name):
		self.driver.find_element_by_css_selector('.icon.icon-menu').click()
		sleep(0.5)
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@placeholder="输入关键字..."]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@placeholder="输入关键字..."]').send_keys(name)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@class="searchResult"]//span[@class="text-truncate"]'),name))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@class="searchResult"]//span[@class="text-truncate"]').click()

	def sp_ck(self):
		self.driver.find_element_by_css_selector('.item-title').click()

	def sp_qx(self):
		self.driver.find_element_by_css_selector('.button.button-big.button-fill.bg-white.details').click()

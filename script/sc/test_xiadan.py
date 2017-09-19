from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,random,os
sys.path.append("../page_obj")
from page_obj.pc_daoru import daoru
from page_obj.page_sc import sc

class qxTest(unittest.TestCase):
	'''权限-充值测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_xd(self):

		#新建密码编号客户
		sc(self.driver).user_login()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("新增客户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="cname"]')))
		sleep(0.5)
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		bh1 = str(a) + str(b)
		self.driver.find_element_by_xpath('//*[@data-role="cname"]').send_keys(name1)
		self.driver.find_element_by_xpath('//*[@data-option="bh"]//input').send_keys(bh1)
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-option="upwd"]//input')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-option="upwd"]//input').send_keys(123456)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)

		#新建两商品一套餐
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("商品库存").click()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增商品").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '商品' + str(b)
		self.driver.find_element_by_xpath('//*[@data-role="gname"]').send_keys(name2)
		self.driver.find_element_by_xpath('//*[@data-role="sellprice"]').send_keys(20)
		self.driver.find_element_by_link_text("库存信息").click()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').clear()
		self.driver.find_element_by_xpath('//*[@data-role="currentStock"]').send_keys(50)
		self.driver.find_element_by_xpath("//*[text()='大屏展示']/../span").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增商品").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name3 = str(a) + '商品' + str(b)
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
		#新增套餐
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("新增套餐").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-role="gname"]')))
		sleep(0.5)
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name4 = str(a) + '套餐' + str(b)
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
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		self.driver.find_element_by_xpath('//tr[2]//div[@class="lcs_cursor"]').click()
		sleep(1)
		self.driver.find_element_by_xpath("//a[2]/span/span/small").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.title'),name4))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.lcs_cursor').click()
		sleep(1)


		#进入商城下单
		#三个全加入购物车，然后删除一个，最后结算
		sc(self.driver).loginsc(bh1)
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).tj_sp2()
		sc(self.driver).clickdw()
		sc(self.driver).jr_gwc()
		sc(self.driver).tj_sp3()
		sc(self.driver).jr_gwc()
		sc(self.driver).shdz1()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"3"))
		sleep(0.5)
		sc(self.driver).clicksc()
		# WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsPrice'),"240"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.uTel'),"13140023070"))
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.item-subtitle.uAddress'),"河南郑州"))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uTel').click()
		sc(self.driver).shdz2()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"购物车空空如也"))
		sleep(0.5)
		sc(self.driver).sc_dd()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"￥240"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥240[\s\S]*")


		#pc端验证订单并转为销售单
		sc(self.driver).user_login()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("订单历史").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.title'),name1))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".title").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"销售订单 [未完成]"))
		sleep(1)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*%s[\s\S]*来　源：商城[\s\S]*河南商丘[\s\S]*13523148316[\s\S]*尾　款：240[\s\S]*备注：尽快送货[\s\S]*总计： 240[\s\S]*" % name1)
		self.driver.find_element_by_link_text("转为销售单").click()
		self.driver.find_element_by_link_text("确定").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"实收：240"))
		sleep(0.5)
		self.driver.find_element_by_xpath('//nav/div[2]//*[@class="bg-blue-600 white submit"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"保存成功"))


		#再次商城验证订单
		sc(self.driver).loginsc(bh1)
		sc(self.driver).sc_dd()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"暂无数据"))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@href="#already"]').click()
		sleep(0.5)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"￥240"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥240[\s\S]*")

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()



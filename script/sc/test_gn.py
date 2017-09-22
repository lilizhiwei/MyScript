from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os,random
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class qxTest(unittest.TestCase):
	'''权限-充值测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1kg(self):
		#创建数据，然后pc端关闭功能，然后商城验证，最后pc端还原
		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '商品1' + str(b)
		sc(self.driver).cj_sp1(name2)
		#上架
		self.driver.find_element_by_css_selector('.lcs_cursor').click()

		#关闭商店开关
		sc(self.driver).sz_sc()
		sc(self.driver).sc_kg()
		sc(self.driver).sc_szcg()


		#商城验证
		self.driver.get('http://lilizhiwei.yyddd.com/')
		self.driver.set_window_size(375,667)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"您要访问网站被关闭！"))
		sleep(0.5)


		#pc端还原
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).sc_kg()
		sc(self.driver).sc_nmfw()
		sc(self.driver).sc_szcg()

	def test_2nmfw(self):

		#商城验证
		self.driver.get('http://lilizhiwei.yyddd.com/')
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"登录到微商城"))
		sleep(0.5)


		#pc端还原
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).sc_nmfw()
		sc(self.driver).sc_nmxd()
		sc(self.driver).sc_szcg()

	def test_3nmxd(self):

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"1"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"登录到微商城"))
		sleep(0.5)


		#pc端还原
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).sc_nmxd()
		sc(self.driver).sc_zskc()
		sc(self.driver).sc_fkc()
		sc(self.driver).sc_szcg()
		sleep(1)

	def test_4kc(self):

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='row no-gutter gStock hide']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@class='row no-gutter gStock hide']").get_attribute("class"))
		sc(self.driver).sp_sl()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.goodsNumber')))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"库存不足"))
		sleep(0.5)

		#pc端还原
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).sc_zskc()
		sc(self.driver).sc_fkc()
		sc(self.driver).sc_yysj()
		sc(self.driver).xg_sj1("01:00")
		sc(self.driver).xg_sj2("02:00")
		sc(self.driver).xg_bc()
		sc(self.driver).sc_szcg()
		sleep(1)

	def test_5yysj(self):

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.goodsNumber')))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		sc(self.driver).xd_sb()

		#pc端修改
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).xg_sj1("23:00")
		sc(self.driver).xg_bc()
		sc(self.driver).sc_szcg()
		sleep(1)

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.goodsNumber')))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		sc(self.driver).xd_sb()

		#pc端修改
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).xg_sj1("22:00")
		sc(self.driver).xg_sj2("20:00")
		sc(self.driver).xg_bc()
		sc(self.driver).sc_szcg()
		sleep(1)

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.goodsNumber')))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"购物车空空如也"))
		sleep(0.5)

		#pc端还原
		sc(self.driver).user_login()
		sc(self.driver).sz_sc()
		sc(self.driver).sc_yysj()
		sc(self.driver).xg_sj1("00:00")
		sc(self.driver).xg_sj2("24:00")
		sc(self.driver).xg_bc()
		sc(self.driver).sc_szcg()
		sleep(1)

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
	
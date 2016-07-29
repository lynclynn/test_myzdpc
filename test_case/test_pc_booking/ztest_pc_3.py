#-*- coding:utf-8 -*-


import unittest,time 
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

t=1
#time.sleep(1)

driver= webdriver.Firefox()

#driver.get('http://pc.dev.mingyizd.com/')
driver.get('http://121.40.127.64:8015/')



time.sleep(t*3)

driver.find_element_by_id("homeforkone").click()

time.sleep(t*2)



#js="var q=document.getElementById("service-circuit-home").scrollTop=10000" 
js="var q=document.documentElement.scrollTop=10000"

driver.execute_script(js)

time.sleep(t*2)
driver.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"王"+Keys.RETURN)


print "home input home-search-form "
#.//*[@id='doctor']/div[53]
print u"第一个页面"+driver.title
print driver.current_url

time.sleep(15)
a=driver.find_element_by_xpath("//*[@id='doctor']/div[10]/a[2]")
time.sleep(7)
a.click()



#driver.find_element_by_class_name("doctor").click()


#driver.find_element_by_link_text(u"进入医生详情页").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
print u"第二个页面"+driver.title
print driver.current_url


time.sleep(t*2)

driver.find_element_by_class_name("ml10").click()

time.sleep(t*2)
driver.find_element_by_css_selector("span.account-login").click()
driver.find_element_by_id("UserLoginForm_username").clear()
driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
driver.find_element_by_id("UserLoginForm_password").clear()
driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
driver.find_element_by_id("btnLoginSubmit").click()

#driver.refresh()
time.sleep(3)
driver.find_element_by_class_name("ml10").click()
time.sleep(2)
#xpath=(//input[@id='booking_contact_nam
#driver.find_element_by_xpath("/input[@id='booking_contact_name'])[2]").send_keys(
driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").clear()
driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").send_keys(u"测试wzl")
driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").clear()
driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").send_keys(u"什么病呢")
driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").clear()
now=time.strftime("%Y")
driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").send_keys(u"至少十个字大漠孤烟直长河落日圆"+now)
        #driver.find_element_by_id("btnSubmit").click()
#driver.quit()
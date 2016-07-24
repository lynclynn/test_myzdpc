#-*- coding:utf-8 -*-


import unittest,time 
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



driver= webdriver.Firefox()

driver.get('http://pc.dev.mingyizd.com/')


driver.find_element_by_id("homeforkone").click()

driver.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"王长希"+Keys.RETURN)
print "imput "
#.//*[@id='doctor']/div[53]
time.sleep(2)
#driver.find_element_by_xpath("//*[@id='doctor']/div[1]/a[1]").click()

#driver.find_element_by_class_name("doctor").click()
#
#driver.find_element_by_link_text(u"进入医生详情页").click()



driver.close()
#-*- coding:utf-8 -*-


#Function:
#Author：智林
#Date：20160719
#Version：1.0

import unittest,time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class test_myzdpc(unittest.TestCase):
    '''
    test:myzdpc
    '''


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.mingyizhudao.com/"
        #self.browser.get('http://pc.dev.mingyizd.com/')
        #self.assertIn(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网', self.browser.title)
        
        #self.verificationErrors = []
        #self.accept_next_alert = True


    def test_pc_0(self):
        '''
        hitest:testPageTitle
        '''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()

      

    def testDown(self):
        pass




if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(test_myzdpc("test_pc_0"))
    
    #now time
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #filename
    filename = '/usr/local/test_myzdpc/report/'+now+'result.html'
    
    
    #report dir
    fp=open(filename,'wb')
    
    print fp 
    #report
    runner=HTMLTestRunner(stream=fp,title='test report',description='test case :')  
    runner.run(testunit)
    fp.close()

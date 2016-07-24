# -*- coding: utf-8 -*-


#Function:
#Author：智林
#Date：20160719
#Version：1.0

import unittest,time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


class test_myzdpc_login(unittest.TestCase):
    ''' 测试登录'''


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.addCleanup(self.browser.quit)

        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.base_url = "http://pc.dev.mingyizd.com/"

        #关闭0元间名医

        #self.browser.find_element_by_id("homeforkone").click()

        #self.browser.get('http://pc.dev.mingyizd.com/')
        
        
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_pc_0(self):
        ''' 账号密码正确登录 '''

        #self.assertEqual(self.driver.title,u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀')

        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_link_text(u"登录").click()

        time.sleep(0.5)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()


        time.sleep(0.2)

        driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/image/loginsuccess.jpg")
        #/usr/local/test_myzdpc/report/result.jpg

        driver.find_element_by_id("logout").click()
        driver.close()



    def test_pc_1(self):
        ''' 密码不正确'''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()

        time.sleep(0.5)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        #密码不正确
        driver.find_element_by_id("UserLoginForm_password").send_keys("2060718")

        driver.find_element_by_id("btnLoginSubmit").click()

        text=driver.find_element_by_class_name("error").text
        self.assertEqual(text,u"登录密码不正确",u"abc")
        #//*[@id='loginModal']/div/div/div/div[1]/button

        driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/image/wrongpassword.jpg")

        #关闭
        driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div/div[1]/button").click()
        #driver.find_element_by_class_name("close").click()

        #主页搜索
        #self.browser.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"王长希"+Keys.RETURN)

        #跳转到医生页面
        #self.browser.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")

        #点击预约

        #self.browser.find_element_by_class_name("ml10").click()



        print "密码不正确测试通过"

    def test_pc_2(self):
        '''  密码长度小于4位'''

        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()

        time.sleep(0.5)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()

        #密码小于4位
        driver.find_element_by_id("UserLoginForm_password").send_keys("21")


        driver.find_element_by_id("btnLoginSubmit").click()
        #text=driver.find_element_by_class_name("error").text
        text=driver.find_element_by_id("UserLoginForm_password-error").text
        time.sleep(1)
       
        self.assertEqual(text,u"登录密码最短为4个字符",u"4 个字的密码")
        driver.close()
        driver.quit()

        #.//*[@id='loginModal']/div/div/div/div[1]/button

    def test_pc_3(self):
        ''' 页面跳转:找名医-->找医院-->患者故事-->公益手术-->关于我们'''

        driver = self.driver
        driver.get(self.base_url + "/")

        time.sleep(0.5)

        #主页：三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网
        #找名医：名医主刀_三甲医院名医,专家,主任医生手术,床位预约,网上挂号,手机APP
        #找医院：国内医院排行榜,医院大全,哪家医院好,床位预约_名医主刀网
        #找患者故事：手术直通车真实案例,患者故事_名医主刀网

        #关于我们：关于我们_名医主刀网

        #找名医
        driver.find_element_by_link_text(u"找名医").click()

        time.sleep(3)

        text=driver.title
        print text
        
        print "页面跳转"
        self.assertIn('专家',text,"这是什么问题")
        #url="http://pc.dev.mingyizd.com/doctor/findexpert"
        #print  driver.getCurrentUrl()
        print driver.current_url
        #self.assertEqual(url,"http://pc.dev.mingyizd.com/doctor/findexpert","Url is right ")
        
        driver.quit()


    def testDown(self):
        self.driver.quit()




if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(test_myzdpc_login("test_pc_0"))
    testunit.addTest(test_myzdpc_login("test_pc_1"))
    testunit.addTest(test_myzdpc_login("test_pc_2"))
    testunit.addTest(test_myzdpc_login("test_pc_3"))
    #testunit.addTest(test_myzdpc("test_pc_4"))
    
    #now time
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #filename
    filename = '/usr/local/test_myzdpc/report/'+now+'_result.html'
    
    
    #report dir
    fp=open(filename,'wb')
    
    print fp 
    #report
    runner=HTMLTestRunner(stream=fp,title='名医主刀PC测试报告',description='测试登录')  
    runner.run(testunit)
    fp.close()

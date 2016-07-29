# -*- coding: utf-8 -*-


#Function:测试登录
#Author：Lynn
#Date：20160719
#Version：1.0

import unittest,time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#休眠时间
t=1
#time.sleep(1)

class test_myzdpc_login(unittest.TestCase):
    ''' 测试登录'''


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.addCleanup(self.browser.quit)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #self.base_url = "http://pc.dev.mingyizd.com/"
        #测试
        self.base_url = "http://121.40.127.64:8015/"      
        #生产
        #self.base_url = "http://www.mingyizhudao.com/" 

        
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_pc_0(self):
        ''' 账号密码正确登录 '''
        #self.driver.get('http://pc.dev.mingyizd.com/')
        #self.assertEqual(self.driver.title,u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀')
        #关闭0元问名医
  
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_id("homeforkone").click()

        driver.find_element_by_link_text(u"登录").click()
        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()


        time.sleep(t)
        #截图
        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/image/loginsuccess.jpg")
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\login_success.jpg")

        #driver.find_element_by_id("logout").click()
        driver.close()

    def test_pc_1(self):
        ''' 账号不正确'''


        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("homeforkone").click()
        
        driver.find_element_by_link_text(u"登录").click()

        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        #账号不正确
        driver.find_element_by_id("UserLoginForm_username").send_keys("182175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()

        time.sleep(3*t)
        #UserLoginForm_username_em_
        #//*[@id='loginModal']/div/div/div/div[1]/button
        text=driver.find_element_by_class_name("error").text
        print text
        self.assertEqual(text,u"该用户名不存在",u"账号不正确")
        print "账号不正确测试通过"
        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/image/wrongpassword.jpg")
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\account_isnot.jpg")


        #关闭
        #driver.find_element_by_class_name("close").click()

        driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div/div[1]/button").click()
    
        driver.close()




    def test_pc_2(self):
        ''' 密码不正确'''


        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("homeforkone").click()
        driver.find_element_by_link_text(u"登录").click()

        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        #密码不正确
        driver.find_element_by_id("UserLoginForm_password").send_keys("2060718")
        driver.find_element_by_id("btnLoginSubmit").click()

        time.sleep(3*t)

        text=driver.find_element_by_class_name("error").text
        self.assertEqual(text,u"登录密码不正确",u"登录密码测试")

        print "密码不正确测试通过"

        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/image/wrongpassword.jpg")
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\wrong_password.jpg")


        #关闭
        driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div/div[1]/button").click()
        #driver.find_element_by_class_name("close").click()

        driver.close()

    def test_pc_3(self):
        '''  密码长度小于4位'''

        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("homeforkone").click()
        driver.find_element_by_link_text(u"登录").click()

        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()

        #密码小于4位
        driver.find_element_by_id("UserLoginForm_password").send_keys("213")


        driver.find_element_by_id("btnLoginSubmit").click()
        #text=driver.find_element_by_class_name("error").text
        time.sleep(1)
        text=driver.find_element_by_id("UserLoginForm_password-error").text
        time.sleep(t)
       
        self.assertEqual(text,u"登录密码最短为4个字符",u"4 个字的密码")
        driver.close()
        driver.quit()
    


  #  def testDown(self):
  #      self.driver.quit()



if __name__ == '__main__':

    print '测试开始'
    testunit=unittest.TestSuite()
    testunit.addTest(test_myzdpc_login("test_pc_0"))
    testunit.addTest(test_myzdpc_login("test_pc_1"))
    testunit.addTest(test_myzdpc_login("test_pc_2"))
    testunit.addTest(test_myzdpc_login("test_pc_3"))
    #testunit.addTest(test_myzdpc("test_pc_4"))
    
    #now time
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #filename
    #mac:
    #filename = '/usr/local/test_myzdpc/report/'+now+'_login.html'
    #win
    #E:\\test_myzdpc\\test_myzdpc\\report\\

    filename = 'E:\\test_myzdpc\\test_myzdpc\\report\\'+now+'_login.html'
       
    #report dir
    fp=open(filename,'wb')
    #report
    runner=HTMLTestRunner(stream=fp,title='名医主刀PC测试报告',description='测试登录')  
    runner.run(testunit)
    print '\n测试结束'

    fp.close()

#----------END ---------------
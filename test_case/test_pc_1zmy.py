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


class test_zmy(unittest.TestCase):
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
    testunit.addTest(test_zmy("test_pc_0"))
    #testunit.addTest(test_myzdpc("test_pc_1"))
    #testunit.addTest(test_myzdpc("test_pc_2"))
    #testunit.addTest(test_myzdpc("test_pc_3"))
    #testunit.addTest(test_myzdpc("test_pc_4"))
    
    #now time
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #filename
    filename = '/usr/local/test_myzdpc/report/'+now+'ZMY_result.html'
    
    
    #report dir
    fp=open(filename,'wb')
    
    print fp 
    #report
    runner=HTMLTestRunner(stream=fp,title='名医主刀PC测试报告',description='测试登录')  
    runner.run(testunit)
    fp.close()

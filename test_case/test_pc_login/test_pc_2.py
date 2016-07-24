#-*- coding:utf-8 -*-


#Function:
#Author：智林
#Date：20160719
#Version：1.0

import unittest,time 
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 





class yymy(unittest.TestCase):
    ''' 预约名医'''


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        '''
        hitest:testPageTitle
        '''

        self.browser.get('http://pc.dev.mingyizd.com/')

        try:
            self.assertIn(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医', self.browser.title)
        except AssertionError as msg:
            print(msg)
        else:
            print("good")


        WebDriverWait(self.browser,1,0.5).until(EC.title_is(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网'))

        
        #退出
        #driver.find_element_by_id("logout").click()



        time.sleep(0.5)

        #关闭O元弹窗

        self.browser.find_element_by_id("homeforkone").click()





        #在线咨询
        #self.browser.find_element_by_class_name("qiao-icon-head").click()

        #size = self.browser.find_element_by_class_name("form-control input-area disease-name").size
        
        #输入框 
        #.//*[@id='home-search-form']/div/input

        self.browser.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"王长希"+Keys.RETURN)

        time.sleep(1)

        #//*[@id='doctor']/div[53]
        #.//*[@id='doctor']/div[5]/a[2]

        #self.browser.find_element_by_id("search-display").click()

        self.browser.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")

        #self.browser.switch_to.window[1]

        time.sleep(1)
        self.browser.find_element_by_class_name("ml10").click()


        time.sleep(1)
        #账号登录
        self.browser.find_element_by_css_selector("span.account-login").click()
        self.browser.find_element_by_id("UserLoginForm_username").clear()
        self.browser.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        self.browser.find_element_by_id("UserLoginForm_password").clear()
        self.browser.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        self.browser.find_element_by_id("btnLoginSubmit").click()

        #pull-right clearhistory mt10
        time.sleep(2)

       

        self.browser.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")

        #self.browser.find_element_by_xpath("//*[@id='doctor']/div/a[2]").click()

        #self.browser.find_element_by_class_name("doctor").click()
        # .//*[@id='doctor']/div/a[2]
        #.//*[@id='doctor']/div[2]/a[2]
        #.//*[@id='doctor']/div[4]/a[2]
        # .//*[@id='doctor']/div[6]/a[2]
        #print size

        self.browser.refresh()

        time.sleep(2)
        self.browser.find_element_by_class_name("ml10").click()

        time.sleep(5)

        #xpath=(//input[@id='booking_contact_name'])[2]

        #self.browser.find_element_by_xpath("/input[@id='booking_contact_name'])[2]").send_keys(u"abc")

        self.browser.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").clear()
        self.browser.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").send_keys(u"测试wzl")
        self.browser.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").clear()
        self.browser.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").send_keys(u"啥病呢")
        self.browser.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").clear()
        self.browser.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").send_keys(u"大饼小兵啦啦啦啦啦啦诗歌子流利")
        #self.browser.find_element_by_id("btnSubmit").click()

        #self.browser.find_element_by_id("checkbox").click()

        self.browser.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()

        #获取提交窗口句柄
        win1=self.browser.current_window_handle

        time.sleep(3)
        self.browser.find_element_by_xpath(u"(//a[contains(text(),'名医主刀在线用户协议')])[2]").click()

        #获得所有窗口句柄
        all_handles = self.browser.window_handles

        #跳转到协议查看界面

        #self.browser.find_element_by_class_name("w25 contactus").text


        for handle in all_handles:
            if handle != win1:
                self.browser.switch_to.window(handle)
                print ('zhuyemian')
                time.sleep(2)
                self.browser.close()

        for handle in all_handles:
            if handle == win1:
                self.browser.switch_to.window(handle)
                self.browser.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()
                self.browser.find_element_by_id("btnSubmit").click()
                
                #//*[@id='content']/div[2]/div/div[2]/div[2]/div/div[1]/div/div[1]/a[1]

                #self.browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/div[2]/div/div[1]/div/div[1]/a[1]").click()

                time.sleep(2)

                #btn btn-yes mr20 w150p

                #href="/booking/uploadFile/1310"
                
                #self.browser.find_element_by_link_text(u"上传影像资料").send_keys("/usr/local/test_myzdpc/report/result.jpg")

                 # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #self.assertEqual(u"错误信息: 文件名重复!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #self.browser.find_element_by_css_selector("#rt_rt_1aobnqknn1fai1nf85i1e0ds9c6 > input[name=\"file\"]").click()
                #self.assertEqual(u"错误信息: 请选择jpg/jpeg/png或gif格式的图片!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #self.browser.find_element_by_id("btnSubmitBooking").click()
    



                time.sleep(2)


        self.browser.switch_to
        time.sleep(2)        
        self.browser.get_screenshot_as_file("/usr/local/test_myzdpc/report/result.jpg")

        #booking_contact_name

        time.sleep(2)





        #form-control input-area disease-name



        #鼠标右击
        #right_click = self.browser.find_element_by_link_text(u"找名医")
        #ActionChains(self.browser).context_click(right_click).perform()

        #time.sleep(5)


        self.browser.get('http://pc.dev.mingyizd.com/')


        #悬停
        #above =self.browser.find_element_by_class_name("waike-home plline")
        #外科
        above =self.browser.find_element_by_xpath("//*[@id='home']/div/div/div/a[1]/div/div")
        # 骨科  //*[@id='home']/div/div/div/a[2]/div/div
        ActionChains(self.browser).move_to_element(above).perform()

        time.sleep(1)
        above =self.browser.find_element_by_xpath("//*[@id='home']/div/div/div/a[2]/div/div")
        ActionChains(self.browser).move_to_element(above).perform()

        time.sleep(1)

        above =self.browser.find_element_by_xpath("//*[@id='home']/div/div/div/a[3]/div/div")
        ActionChains(self.browser).move_to_element(above).perform()

        #time.sleep(1)

        self.browser.get_screenshot_as_file("/usr/local/test_myzdpc/report/result.jpg")



        #results=u"王长希"
        #keyword=u"王"

        #js="var a=document.getElementById('home-search-form').value("results");"
        #js = "ajaxSearchByKeyWord(keywords)"


        #self.browser.execute_script(js)

        #self.browser.get_screenshot_as_file("/usr/local/test_myzdpc/report/result.jpg")
        self.browser.set_window_size(1200,600)

        js="window.scrollTo(300,300);"

        self.browser.execute_script(js)

        time.sleep(6)


        js="window.scrollTo(0,0);"

        self.browser.execute_script(js)


        time.sleep(6)






    def testDown(self):
        self.driver.quit()




if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(myzdpcTestCase("testPageTitle"))
    #report dir
    fp=open('/usr/local/test_myzdpc/report/result.html','wb')
    print fp 
    #report
    runner=HTMLTestRunner(stream=fp,title='test report',description='test case :')  
    runner.run(testunit)
    fp.close()

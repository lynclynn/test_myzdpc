#-*- coding:utf-8 -*-


#Function:测试预约医生
#Author：Lynn
#Date：20160719
#Version：1.0

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
#time.sleep(t)

class doctor(unittest.TestCase):
    ''' 预约名医'''


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        #self.addCleanup(self.driver.quit)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        #self.base_url = "http://pc.dev.mingyizd.com/"
        self.base_url = "http://121.40.127.64:8015/"
        #self.base_url = "http://www.mingyizhudao.com/" 


        self.verificationErrors = []
        self.accept_next_alert = True

        #try:
        #    self.assertIn(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医', self.driver.title)
        #except AssertionError as msg:
        #    print(msg)
        #else:
        #    print("good")

    def test_book_doctor(self):
        '''
        预约名医
        '''
		
        #WebDriverWait(self.driver,1,0.5).until(EC.title_is(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网'))

        #退出
        #driver.find_element_by_id("logout").click()
        driver = self.driver

        #self.driver = webdriver.Firefox()
        driver .get(self.base_url + "/")

        time.sleep(2)

        #关闭O元弹窗
        driver.find_element_by_id("homeforkone").click()

        #在线咨询
        #driver.find_element_by_class_name("qiao-icon-head").click()

        #size = driver.find_element_by_class_name("form-control input-area disease-name").size

        #driver.find_element_by_xpath("//*[@id='doctor']/div/a[2]").click()
        #driver.find_element_by_class_name("doctor").click()
        # .//*[@id='doctor']/div/a[2]
        #.//*[@id='doctor']/div[2]/a[2]
        #.//*[@id='doctor']/div[4]/a[2]
        # .//*[@id='doctor']/div[6]/a[2]
        #print size
        
        
        #输入框 
        #.//*[@id='home-search-form']/div/input
        driver.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"王长希"+Keys.RETURN)

        time.sleep(t)

        #//*[@id='doctor']/div[53]
        #.//*[@id='doctor']/div[5]/a[2]

        #driver.find_element_by_id("search-display").click()
        #driver.switch_to.window[1]

        #driver.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")
        driver.get('http://121.40.127.64:8015/'+ "/doctor/1657/")

        time.sleep(t)
        #点击预约某某医生
        driver.find_element_by_class_name("ml10").click()


        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()

        time.sleep(t*2)

       
        #driver.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")
        driver.get('http://121.40.127.64:8015/'+ "/doctor/1657/")

        #刷新页面
        driver.refresh()

        time.sleep(t)
        driver.find_element_by_class_name("ml10").click()

        time.sleep(t*2)

        #输入预约单
        driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").send_keys(u"测试自动预约医生")
        driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").send_keys(u"来自IT部")
        driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").clear()
       	now=time.strftime("%Y-%m-%d")

        driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").send_keys(now+u":10个字-今天是个好天气")
        #driver.find_element_by_id("btnSubmit").click()
        #driver.find_element_by_id("checkbox").click()

        #按钮:我已经同意……
        driver.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()

        #跳转到服务协议页面
        #获取提交窗口句柄
        win1=driver.current_window_handle

        time.sleep(t*3)
        driver.find_element_by_xpath(u"(//a[contains(text(),'名医主刀在线用户协议')])[2]").click()

        #获得所有窗口句柄
        all_handles = driver.window_handles

        #跳转到协议查看界面
        #driver.find_element_by_class_name("w25 contactus").text


        for handle in all_handles:
            if handle != win1:
                driver.switch_to.window(handle)
                print ('提交预约医生成功')
                time.sleep(t*1)
                driver.close()

        for handle in all_handles:
            if handle == win1:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()
                driver.find_element_by_id("btnSubmit").click()
                
        #上传图像
                #btn btn-yes mr20 w150p
                #href="/booking/uploadFile/1310"
                
                #driver.find_element_by_link_text(u"上传影像资料").send_keys("/usr/local/test_myzdpc/report/result.jpg")

                # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #self.assertEqual(u"错误信息: 文件名重复!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #driver.find_element_by_css_selector("#rt_rt_1aobnqknn1fai1nf85i1e0ds9c6 > input[name=\"file\"]").click()
                #self.assertEqual(u"错误信息: 请选择jpg/jpeg/png或gif格式的图片!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
                #driver.find_element_by_id("btnSubmitBooking").click()
    
        time.sleep(2)
     	#截图：预约结果
        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/result.jpg")
        #<div class="color-status text12 pull-left">预约单：DR160729164359</div>
        #.//*[@id='content']/div[2]/div/div[2]/div[1]/div/div[1]
        BookingID=driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/div[1]/div/div[1]").text
        print "BookingID:"+BookingID
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\result_doctor.jpg")


        driver.quit()





  #  def testDown(self):
  #      self.driver.quit()




if __name__ == '__main__':

    print '测试开始' 
    testunit=unittest.TestSuite()
    testunit.addTest(doctor("test_book_doctor"))

    
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #report dir
    #fp=open('/usr/local/test_myzdpc/report/result.html','wb')
    
    filename = 'E:\\test_myzdpc\\test_myzdpc\\report\\'+now+'_booking_doctor.html'
    fp=open(filename,'wb')


    #report
    runner=HTMLTestRunner(stream=fp,title='test 预约名医',description='测试结果')  
    runner.run(testunit)
    print '\n测试结束'

    fp.close()


#------------------END-----------------
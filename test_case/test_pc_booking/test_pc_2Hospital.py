#-*- coding:utf-8 -*-


#Function:测试预约科室
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

class hospital(unittest.TestCase):
    ''' 预约医院'''


    def setUp(self):

        self.driver = webdriver.Firefox()
        #self.addCleanup(self.driver.quit)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #self.base_url = "http://pc.dev.mingyizd.com/"
        self.base_url = "http://121.40.127.64:8015/"
        #self.base_url = "http://www.mingyizhudao.com/" 

        #try:
        #    self.assertIn(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医', self.driver.title)
        #except AssertionError as msg:
        #    print(msg)
        #else:
        #    print("good")

    def test_book_hospital(self):
        '''
        预约医院
        '''
		#WebDriverWait(self.driver,1,0.5).until(EC.title_is(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网'))

        #退出
        #driver.find_element_by_id("logout").click()

        #self.driver = webdriver.Firefox()
        driver=self.driver
        driver.get(self.base_url + "/")

        time.sleep(2)

        #关闭O元弹窗

        driver.find_element_by_id("homeforkone").click()


        #输入医院啦

        #//*[@id='hospital']/div[4]/a[1]/span
        #driver.find_element_by_xpath("//*[@id='hospital']/div[4]/a[1]/span").click()
        driver.find_element_by_xpath("//*[@id='home-search-form']/div/input").send_keys(u"北京"+Keys.RETURN)
        time.sleep(t)

        driver.get('http://121.40.127.64:8015/'+ "/hospital/11")
        
        #driver.get('http://www.mingyizhudao.com/'+ "/hospital/11")



        #driver.switch_to.window[1]

        time.sleep(6*t)
        driver.find_element_by_xpath("//*[@id='booking692']/div[2]/button").click()

        #driver.find_element_by_class_name("bookingBtn btn btn-yes text-center").click()


        time.sleep(t)
        #账号登录
        driver.find_element_by_css_selector("span.account-login").click()
        driver.find_element_by_id("UserLoginForm_username").clear()
        driver.find_element_by_id("UserLoginForm_username").send_keys("18217175942")
        driver.find_element_by_id("UserLoginForm_password").clear()
        driver.find_element_by_id("UserLoginForm_password").send_keys("20160718")
        driver.find_element_by_id("btnLoginSubmit").click()

        #pull-right clearhistory mt10
        time.sleep(t*2)

       

        #driver.get('http://pc.dev.mingyizd.com/'+ "/doctor/1657/")
        driver.get('http://121.40.127.64:8015/'+ "/hospital/11")
        #driver.get('http://www.mingyizhudao.com/'+ "/hospital/11")
  

        #driver.find_element_by_xpath("//*[@id='doctor']/div/a[2]").click()

        #driver.find_element_by_class_name("doctor").click()
        # .//*[@id='doctor']/div/a[2]
        #.//*[@id='doctor']/div[2]/a[2]
        #.//*[@id='doctor']/div[4]/a[2]
        # .//*[@id='doctor']/div[6]/a[2]
        #print size

        #driver.refresh()

        time.sleep(t)
        #driver.find_element_by_class_name("bookingBtn btn btn-yes text-center").click()

        driver.find_element_by_xpath("//*[@id='booking692']/div[2]/button").click()
        #//*[@id='booking692']/div[2]/button

        time.sleep(t*5)

        #xpath=(//input[@id='booking_contact_name'])[2]

        #driver.find_element_by_xpath("/input[@id='booking_contact_name'])[2]").send_keys(u"abc")

        driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='booking_contact_name'])[2]").send_keys(u"测试自动预约医院")
        driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='booking_disease_name'])[2]").send_keys(u"来自IT部")
        driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").clear()
       	now=time.strftime("%Y-%m-%d")

        driver.find_element_by_xpath("(//textarea[@id='booking_disease_detail'])[2]").send_keys(now+u"10个字：客服妹子好，你们辛苦了！！！")
        #driver.find_element_by_id("btnSubmit").click()

        #driver.find_element_by_id("checkbox").click()

        driver.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()


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
                print ('提交预约科室成功啦')
                time.sleep(t*2)
                driver.close()

        for handle in all_handles:
            if handle == win1:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath("(//input[@name='booking[terms]'])[2]").click()
                driver.find_element_by_id("btnSubmit").click()
                
                #//*[@id='content']/div[2]/div/div[2]/div[2]/div/div[1]/div/div[1]/a[1]

                #driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/div[2]/div/div[1]/div/div[1]/a[1]").click()

                time.sleep(2)

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
    

     	#预约结果
        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/result.jpg")
        BookingID=driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div[2]/div[1]/div/div[1]").text
        #.//*[@id='content']/div[2]/div/div[2]/div[1]/div/div[1]
        print "BookingID:"+BookingID
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\result_hospital.jpg")
     


        driver.close()



  #  def testDown(self):
  #      driver.quit()




if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(hospital("test_book_hospital"))
    print "测试开始"
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #report dir
    #fp=open('/usr/local/test_myzdpc/report/result.html','wb')
    
    filename = 'E:\\test_myzdpc\\test_myzdpc\\report\\'+now+'_booking_hospital.html'
    fp=open(filename,'wb')


    #report
    runner=HTMLTestRunner(stream=fp,title='test 预约科室',description='测试结果 :')  
    runner.run(testunit)
    fp.close()

#--------------END--------------
# -*- coding: utf-8 -*-


#Function:测试主页面导航跳转
#Author：Lynn
#Date：20160719
#Version：1.0

import unittest,time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
import sys

t=1

#time.sleep(t)

reload(sys)
sys.setdefaultencoding('utf-8')


class test_homepage_link(unittest.TestCase):
    ''' 测试主页面跳转'''


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.addCleanup(self.browser.quit)
        
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        #self.base_url = "http://pc.dev.mingyizd.com/"
        self.base_url = "http://121.40.127.64:8015/"

        #self.base_url = "http://www.mingyizhudao.com/"      
        
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_pc_0(self):
        ''' 页面跳转:找名医-->找医院-->患者故事-->公益手术-->关于我们'''

        driver = self.driver
        driver.get(self.base_url + "/")

        #关闭0元间名医
        #self.driver.get('http://pc.dev.mingyizd.com/')


        time.sleep(t)
        driver.find_element_by_id("homeforkone").click()

        #主页：三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网
        #找名医：名医主刀_三甲医院名医,专家,主任医生手术,床位预约,网上挂号,手机APP
        #找医院：国内医院排行榜,医院大全,哪家医院好,床位预约_名医主刀网
        #找患者故事：手术直通车真实案例,患者故事_名医主刀网
        #公益手术：名医公益联盟,公益手术申请_名医主刀网
        #关于我们：关于我们_名医主刀网

        #滚动页面到底部
        #js="var q=document.documentElement.scrollTop=10000"
        js="var q=document.documentElement.scrollTop=400"
        driver.execute_script(js)
        time.sleep(2)


        #将滚动条移动到页面100处
        js="var q=document.documentElement.scrollTop=800"
        driver.execute_script(js)
        time.sleep(2)


        #将滚动条移动到页面100处
        js="var q=document.documentElement.scrollTop=1200"
        driver.execute_script(js)
        time.sleep(2)

        #将滚动条移动到页面100处
        js="var q=document.documentElement.scrollTop=1600"
        driver.execute_script(js)
        time.sleep(2)

        #将滚动条移动到页面100处
        js="var q=document.documentElement.scrollTop=1900"
        driver.execute_script(js)
        time.sleep(2)




        #.//*[@id='site-content']/div[4]/div/div/div/div[1]/a/img
        #driver.find_element_by_xpath("//*[@id='site-content']/div[4]/div/div/div/div[1]/a/img").click()
        #time.sleep(2)

        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        time.sleep(2)



        homepage=driver.current_window_handle

        #找名医
        #------1---------
        driver.find_element_by_link_text(u"找名医").click()
        self.assertIn('专家',driver.title,"没有跳转到找名医")

        print "homepage:"+driver.title
        driver.switch_to.window(driver.window_handles[1])

        print "找名医:"+driver.title
        #------2---------

        driver.find_element_by_link_text(u"找医院").click()
        driver.switch_to.window(driver.window_handles[2])

        print "找医院:"+driver.title

        self.assertIn('哪家',driver.title,"没有跳转到找医院")

        #------3---------
        driver.find_element_by_link_text(u"患者故事").click()

        driver.switch_to.window(driver.window_handles[3])

        print "患者故事:"+driver.title
        self.assertIn('患者',driver.title,"2")
        #------4---------

        driver.find_element_by_link_text(u"公益手术").click()

        driver.switch_to.window(driver.window_handles[4])

        print "公益手术:"+driver.title
        self.assertIn('公益手术',driver.title,"")
        
        #------5---------
        driver.find_element_by_link_text(u"关于我们").click()

        driver.switch_to.window(driver.window_handles[5])

        print "关于我们:"+driver.title
        self.assertIn('关于我们',driver.title,"")

        time.sleep(t*2)    
        #url="http://pc.dev.mingyizd.com/doctor/findexpert"
        print driver.current_url
        #self.assertEqual(url,"http://pc.dev.mingyizd.com/doctor/findexpert","Url is right ")

        #调回主页
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        all_handles = driver.window_handles

        #轮播一次
        i = 0
        for handle in all_handles:
            if handle != homepage:
                driver.switch_to.window(handle)
                print '第%d次切换'%i
                print driver.title
                print driver.current_url
                i=i+1
                time.sleep(t*2)
                driver.close()

        time.sleep(2)
        
        #回主页
        for handle in all_handles:
            if handle == homepage:
                driver.switch_to.window(handle)
                print driver.current_url
                print driver.title


    #driver.get('http://pc.dev.mingyizd.com/')
       # driver.get('http://121.40.127.64:8015/')

        #鼠标右击
        #right_click = driver.find_element_by_link_text(u"找名医")
        #ActionChains(driver).context_click(right_click).perform()

        time.sleep(5)

        #悬停
        #above =driver.find_element_by_class_name("waike-home plline")
        
        #外科
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[1]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)

        #骨科  //*[@id='home']/div/div/div/a[2]/div/div
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[2]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)

        #妇产科
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[3]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)

        
        #小儿外科
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[4]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)

        #五官科  //*[@id='home']/div/div/div/a[2]/div/div
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[5]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)
        
        #内科
        above =driver.find_element_by_xpath("//*[@id='home']/div/div/div/a[6]/div/div")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(1)


        #driver.get_screenshot_as_file("/usr/local/test_myzdpc/report/mouseresult.jpg")
        driver.get_screenshot_as_file("E:\\test_myzdpc\\test_myzdpc\\report\\image\\result_mouse.jpg")


        #调用JS
        #results=u"王长希"
        #keyword=u"王"

        #js="var a=document.getElementById('home-search-form').value("results");"
        #js = "ajaxSearchByKeyWord(keywords)"
        #driver.execute_script(js)

        #设置窗口

        # driver.set_window_size(1200,600)
        # js="window.scrollTo(300,300);"
        # driver.execute_script(js)
        # time.sleep(2)

        # js="window.scrollTo(0,0);"
        # driver.execute_script(js)
        # time.sleep(2)


        driver.close()
        driver.quit()


   # def testDown(self):
    #    self.driver.quit()



if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(test_homepage_link("test_pc_0"))
    #testunit.addTest(test_myzdpc("test_pc_1"))
    #testunit.addTest(test_myzdpc("test_pc_2"))
    #testunit.addTest(test_myzdpc("test_pc_3"))
    #testunit.addTest(test_myzdpc("test_pc_4"))
    
    #now time
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    
    #filename

    #E:\\test_myzdpc\\test_myzdpc\\report\\
    #filename = '/usr/local/test_myzdpc/report/'+now+'_testlink.html'
    filename = 'E:\\test_myzdpc\\test_myzdpc\\report\\'+now+'_testlink.html'

    #report dir
    fp=open(filename,'wb')

    #report
    runner=HTMLTestRunner(stream=fp,title='名医主刀PC测试报告-主页面跳转',description='测试主页面跳转')  
    runner.run(testunit)
    fp.close()

#---------------END------------------
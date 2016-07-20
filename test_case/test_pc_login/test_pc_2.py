#-*- coding:utf-8 -*-


#Function:
#Author：智林
#Date：20160719
#Version：1.0

import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner

class myzdpcTestCase(unittest.TestCase):
    '''
    test:myzd
    '''


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        '''
        hitest:testPageTitle
        '''

        self.browser.get('http://pc.dev.mingyizd.com/')
        self.assertIn(u'三甲医院手术预约,专家,主任医生手术,床位预约_名医主刀网', self.browser.title)

    def testDown(self):
        pass




if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(myzdpcTestCase("testPageTitle"))
    #report dir
    fp=open('./test_myzdpc/report/result.html','wb')
    print fp 
    #report
    runner=HTMLTestRunner(stream=fp,title='test report',description='test case :')  
    runner.run(testunit)
    fp.close()

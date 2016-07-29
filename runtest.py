# -*- coding: utf-8 -*-

#Function:test 名医主刀PC网站
#Author：Lynn
#Date：20160725
#Version：1.0

import unittest,os,time
from HTMLTestRunner import HTMLTestRunner


t=1
#tims.sleep(t)


#print os.sys.path
#定义测试报告，用例目录
#Mac:		 report_dir='./report'
#Windows:
report_dir = 'E:\\test_myzdpc\\test_myzdpc\\report\\'

#Mac: 		test_dir ='./test_case'
#Windows:
test_dir ='E:\\test_myzdpc\\test_myzdpc\\test_case\\'


discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_pc_*.py')



if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_dir+'/'+now+'_project_result.html'
    fp=open(filename,'wb')
    print "测试开始"

    runner=HTMLTestRunner(stream=fp,title=u'myzdpc测试报告',description='用例执行情况:')  
    runner.run(discover)
    fp.close()

#------END ------
# -*- coding: utf-8 -*-


import unittest,os,time

from HTMLTestRunner import HTMLTestRunner



#print os.sys.path
#定义测试用例的目录为当前目录
report_dir='./report'
test_dir ='./test_case'


discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_pc_*.py')





if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S")

    filename = report_dir+'/'+now+'project_result.html'

    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,title=u'myzdpc测试报告',description='用例执行情况:')  

    #runner = unittest.TextTestRunner()
    runner.run(discover)
    fp.close()



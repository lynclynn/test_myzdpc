#-*- coding:utf-8 -*-

import unittest,os,time

from HTMLTestRunner import HTMLTestRunner



print os.sys.path
#定义测试用例的目录为当前目录
test_dir ='./test_myzdpc/test_case'

print os.sys.path

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')





if __name__ == '__main__':

    now = time.strftime("%Y-%M-%d %H_%M_%S")

    filename = test_dir+'/'+now+'result.html'

    fp=open(filename,'wb')

    runner=HTMLTestRunner(stream=fp,title=u'测试报告',description='用例执行情况:')  

    #runner = unittest.TextTestRunner()
    runner.run(discover)
    fp.close()



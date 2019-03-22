#coding=utf-8
import ddt
import unittest
import sys
sys.path.append('S:\\GraduationProject\\selenium') 
from selenium import webdriver
import traceback
import time
import os
import HTMLTestRunner
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
from log.user_log import UserLog

ex = ExcelUtil()
data = ex.get_data()

#file_name = "S:/GraduationProject/selenium/image/test.png"
#print(file_name)

#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')
        cls.driver.maximize_window()

    def setUp(self):

        self.driver.refresh()
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)


    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"\\report\\"+case_name+".png")
                self.driver.save_screenshot(file_path)
        #print("这个是case的后置条件1")
        self.logger.info("Finished.")
        

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()


    '''
    @ddt.data(
            ['864','ttyuan','123456','code','user_email_error','请输入有效的电子邮箱地址'],
            ['@qq.com','ttyuan','123456','code','user_email_error','请输入有效的电子邮箱地址'],
            ['864@qq.com','ttyuan','123456','code','user_email_error','请输入有效的电子邮箱地址']
        )

    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,file_name,assertCode,assertText = data
        email_error = self.login.register_function(email,username,password,file_name,assertCode,assertText)
        self.assertFalse(email_error,"测试失败")


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"\\report\\"+"first_case1.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is register report1",description=u"测试报告1",verbosity=2)
    runner.run(suite)
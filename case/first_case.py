#coding=utf-8
import ddt
import sys
sys.path.append('S:\\GraduationProject\\selenium') 
from selenium import webdriver
from log.user_log import UserLog
import traceback
import unittest
import time
import os
import HTMLTestRunner
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil

log = UserLog()
logger = log.get_log()

class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = "S:/GraduationProject/selenium/image/test.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.refresh()
        logger.info("this is chrome")
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

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()

    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    def test_login_email_error(self):
        email_error = self.login.login_email_error('1314','user1111@qq.com','111111',self.file_name)
        self.assertFalse(email_error,"测试失败")
        
    def test_login_username_error(self):
        username_error = self.login.login_name_error('12123@qq.com','t1','111111',self.file_name)
        self.assertTrue(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_name_error('11121@qq.com','ss22212','111111',self.file_name)
        self.assertFalse(code_error)
    
    def test_login_password_error(self):
        password_error = self.login.login_name_error('11311@qq.com','ss23222','111111',self.file_name)
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.register_succes('12221@qq.com','2321','111111',self.file_name)
        self.assertFalse(success)
        #self.assert

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"\\report\\"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    #suite.addTest(FirstCase('test_login_code_error'))
    #suite.addTest(FirstCase('test_login_email_error'))
    #suite.addTest(FirstCase('test_login_username_error'))
    #unittest.TextTestRunner().run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is register report",description=u"测试报告",verbosity=2)
    runner.run(suite)

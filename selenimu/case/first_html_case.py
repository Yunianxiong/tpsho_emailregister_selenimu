# coding=utf-8

import unittest

import HTMLTestRunner
from bussiness.email_register_bussiness import Email_register_bussiness


class Htmlreportcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('ceshikais')

    def setUp(self):
        self.erb = Email_register_bussiness('http://192.168.50.131/Home/User/reg/t/email.html')
        print('zheshi qianzhi')

    def tearDown(self):
        print('zheshi houzhi')
        self.erb.driver_close()

    def test_email_error(self):
        str = '请输入正确邮箱'
        error = self.erb.email_login('12', '123456', '123456', '987654321')
        self.assertEqual(error, '请输入正确邮箱', '通过')

    def test_password_error(self):
        # 感叹号不同会报错。。
        str = '密码有效长度为6-16位'
        error = self.erb.email_login('123@qq.cc', '1234', '1234', '987654321')[:-1]
        self.assertEqual(error, str, '通过')

#用HTMLTestRunner生成报告，这个得单独配置一个环境，脱离unittest。
if __name__ == '__main__':
    path = 'D:\pypj\selenimu\\reporets\\firstdd.html'
    suite = unittest.TestSuite()
    suite.addTest(Htmlreportcase('test_password_error'))
    with open(path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='第一次报告', description='测试报告', verbosity=2)
        runner.run(suite)

    """   
    #html_report_path=os.path.join(os.getcwd()+"/reports/"+"frist_case.html")
    path = 'D:\pypj\selenimu\\reporets\\first.html'
    """

#coding=utf-8
import time

import ddt
import unittest
from bussiness.email_register_bussiness import Email_register_bussiness
import HTMLTestRunner
@ddt.ddt
class BaseTest(unittest.TestCase):


    def setUp(self):
        self.erb = Email_register_bussiness('http://192.168.50.131/Home/User/reg/t/email.html')
        print('zheshi qianzhi')

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                #截图,获取用例名字
                case_name=self._testMethodName
                print(case_name)


        self.erb.driver_close()

        print('zheshi houzhi')

    @ddt.data(
        ['123465@qq.cc','123456','123456','565689','请输入正确邮箱'],
        ['123465','123456','123456','565689','请输入正确邮箱']
    )

    @ddt.unpack
    def test_email_error(self,email,password,password_again,res,judge):
        error=self.erb.email_login(email_value=email,password_value=password,
                                   password_again_value=password_again,use_rec_tel_value=res)
        self.assertEqual(error,judge,'通过')

#ddt的原因，可以用其他文件来加载。
if __name__=='__main__':
    unittest.main()
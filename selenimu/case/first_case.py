#coding=utf-8

import ddt
import unittest
from bussiness.email_register_bussiness import Email_register_bussiness


class FirstTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.erb=Email_register_bussiness('http://192.168.50.131/Home/User/reg/t/email.html')

    def setUp(self):
        print('zheshi qianzhi')

    def tearDown(self):
        print('zheshi houzhi')


    def test_email_error(self):
        str='请输入正确邮箱'
        error=self.erb.email_login('12','123456','123456','987654321')
        self.assertEqual(error,'请输入正确邮箱','通过')

if __name__=='__main__':
    unittest.main()
#coding=utf-8
import time
import sys
sys.path.append('D:\pypj\selenimu')
#print(sys.path)
from until.read_excel import handle_excel_data
import unittest
import ddt
from bussiness.email_register_bussiness import Email_register_bussiness
from log.user_log import Use_log
import HTMLTestRunner

@ddt.ddt
class ddt_for_excel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ul = Use_log()
        cls.fl = cls.ul.get_log()

        print('kaishiceshi')

    def setUp(self) -> None:
        self.erb=Email_register_bussiness('http://192.168.50.131/Home/User/reg/t/email.html')
        case_name = self._testMethodName
        self.fl.info(case_name)



    def tearDown(self) -> None:
        time.sleep(2)
        for method_name,error  in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                print(case_name)


        self.erb.driver_close()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.ul.close_handle()
    #从excel加载。
    @ddt.data(*handle_excel_data().get_data())
    @ddt.unpack
    def test_from_excle_caes(self,email, password, password_again, res, error_msg):
        judge_msg=self.erb.email_login(email_value=email,password_value=password,password_again_value=password_again,
                             use_rec_tel_value=res)
        self.assertEqual(judge_msg,error_msg,'通过')


if __name__=='__main__':
    if __name__ == '__main__':
        path = 'D:\pypj\selenimu\\reporets\\ddt.html'
        suite = unittest.TestSuite()
        suite.addTest(ddt_for_excel('test_from_excle_caes'))
        with open(path, 'wb') as f:
            runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='第一次报告', description='测试报告', verbosity=2)
            runner.run(suite)
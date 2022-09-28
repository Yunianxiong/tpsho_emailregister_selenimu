# coding=utf-8

import unittest

import mock

url = 'http://www.baidu.com'
data = {
    'username': '1233',
    'password': '111111111'
}
'''def post_request(url,data):
    res=requests.post(url,data).json()
    return res
'''


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_01(self):
        url = 'http://www.imooc.com/login/regist'
        data = {
            'username': '111111'
        }
        sucess_test = mock.Mock(return_value=data)
        print(sucess_test)
        post_request = sucess_test
        print(post_request)
        res = sucess_test
        print(res.return_value)
        self.assertEqual('111111', res()['username'])


if __name__ == '__main__':
    unittest.mian()

# coding=utf-8
import os
import sys

# 添加工程路径。防止找不到模块
import mock

case_path = os.getcwd()
sys.path.append(case_path)
import unittest
import json


def read_json():
    with open('', '') as f:
        data = json.load(f)
    return data


from Base_request.base_requests import BaseRequest


class TestCaes01(unittest.TestCase):
    def setUp(self) -> None:
        self.br = BaseRequest()

    def tearDown(self) -> None:
        pass

    def test_01(self):
        url = ''
        data = {

        }
        mthod_moci = mock.Mock(return_value=read_json())
        self.br.run_main = mthod_moci
        res = self.br.run_main('get', url, data)

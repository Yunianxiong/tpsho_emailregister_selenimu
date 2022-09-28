# coding=utf-8
import json

import requests

from handle.handleini import HandleInit


class BaseRequest:
    def __init__(self):
        pass

    def send_post(self, url, data, cookie):
        # 这里不能json()，万一是text会报错，这边直接用text获取文本
        response = requests.post(url, data, cookies=cookie).text
        return response

    def send_get(self, url, data, cookie):
        response = requests.get(url=url, params=data, cookies=cookie).text
        return response

    def run_main(self, method, url, data, cookie=None):
        hi = HandleInit()
        base_url = hi.get_value('host')
        complete_url = base_url + url
        if method == 'get':
            res = self.send_get(complete_url, data, cookie)
        elif method == 'post':
            res = self.send_post(complete_url, data, cookie)

        try:
            res = json.loads(res)

        except:
            res = '出错了'
        print(res)
        return res


if __name__ == '__main__':
    url = 'api3/getbanneradvertver2'
    data = {"username": "111111"}
    br = BaseRequest()
    res = br.run_main('post', url, data)
    print(res)

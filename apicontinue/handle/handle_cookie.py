# coding=utf-8
from handle.handle_json import HandeJson


class Handle_cookie:
    def __init__(self):
        self.hj = HandeJson()

    def get_cookie_value(self, key):
        '''

        :param key: 字典的键
        :return: 键对应的值
        '''
        data_cookie = self.hj.read_json('cookie')
        return data_cookie[key]

    def write_cookie(self, key, value):
        '''

        :param key: 字典的键
        :param value: 字典的值
        :return: 返回一个TRUE或者FALSE用于判断是否写入成功
        '''
        data_cookie = self.get_cookie_value(key)
        data_cookie[key] = value
        tf = self.hj.write_json_vale('cookie', data_cookie)
        return tf


if __name__ == '__main__':
    hc = Handle_cookie()
    data = None
    tf = hc.write_cookie('web', data)
    print(tf)

# coding=utf-8
import os
import sys

# 添加工程路径。防止找不到模块
base_path = os.getcwd()
sys.path.append(base_path)
from handle.read_excel import Read_Excel
from Base_request.base_requests import BaseRequest
from handle.handle_result import Hand_result
from handle.handle_cookie import Handle_cookie


class RunMain:
    def __init__(self):
        self.re = Read_Excel()

    def run_case(self):
        # data_value={"newapiid": "ddddddddddddd"}
        row_max = self.re.get_row()
        for i in range(row_max):
            # 这个读excel是从第一行开始算的。
            data = self.re.get_data_row(i + 2)
            is_run = data[2]
            if is_run == 'yes':
                condition=data[3]
                method = data[5]
                url = data[4]
                cookie_opt = data[7]
                header_opt=data[8]
                ex_result_meod = data[9]
                ex_eresult = data[10]
                data_text = data[6]
                # print(ex_eresult)
                # print(f'{method}-{url}-{cookie_opt}-{ex_result_meod}-{data_text}')
                if cookie_opt == 'write':
                    get_cookie = 'web'
                cookie_text = self.cookie_option(cookie_opt, 'web')
                print(cookie_text)
                api_msg = self.get_api_msg(method, url, data_text, cookie_text)
                print(api_msg)
                # print(api_msg['errorCode'])
                if ex_result_meod == 'mec':
                    result_msg = self.get_handle_result_msg(ex_result_meod, url, api_msg['errorCode'])
                    # print(api_msg['errorCode'])
                    # print(result_msg)
                    if api_msg['errorDesc'] == result_msg:
                        fin_result = '用例通过'
                        self.re.write_excel(i + 2, 12, fin_result)
                        print(fin_result)
                    else:
                        fin_result = '用例失败'
                        self.re.write_excel(i + 2, 12, fin_result)
                        self.re.write_excel(i + 2, 13, str(api_msg))
                        print(fin_result)
                if ex_result_meod == 'errorcode':
                    # 这个是直接走excel的。
                    if str(api_msg['errorCode']) == ex_eresult:
                        fin_result = '用例通过'
                        self.re.write_excel(i + 2, 12, fin_result)
                        print(fin_result)
                    else:
                        fin_result = '用例失败'
                        self.re.write_excel(i + 2, 12, fin_result)
                        self.re.write_excel(i + 2, 13, str(api_msg))
                        print(fin_result)
                if ex_result_meod == 'json':

                    if api_msg['errorCode'] == '1000':
                        # 对应result.json的两部分，一个成功，一个失败。分别获取两个字典比较是否为相应的json格式
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    msg = self.get_handle_result_msg(ex_result_meod, url, status_str, api_msg)
                    # print(api_msg)
                    if msg == True:
                        fin_result = '用例通过'
                        self.re.write_excel(i + 2, 12, fin_result)
                        print(fin_result)
                    else:
                        fin_result = '用例失败'
                        self.re.write_excel(i + 2, 12, fin_result)
                        self.re.write_excel(i + 2, 13, str(api_msg))
                        print(fin_result)
            # print(data)

    def get_handle_result_msg(self, ex_result_meod, url, check_msg, json_dict=None):
        '''

        :param ex_result_meod: 预期结果方式
        :param url: 链接
        :param check_msg: 要检查的数据 mec对应的是api_msg['errorCode']的值在code那边找，json是在此基础上判断成功或失败，
        查找对应的状态值，在result那边找并用judge_json判断格式
        :param json_dict: 是api_msg的返回值。链接响应的值
        :return:
        '''
        msg = ''
        ex_result_meod = ex_result_meod
        hs = Hand_result()

        if ex_result_meod == 'mec':
            msg = hs.handl_code_msg(url, check_msg)
            # print(f'--->{msg}')
        elif ex_result_meod == 'json':
            data = hs.get_result_msg(url, check_msg)
            msg = hs.judge_json(data, json_dict)
        return msg

    def get_api_msg(self, method, url, data, cookie=None):
        '''

        :param method: get,post之类的
        :param url: 链接
        :param data: 带入请求的数据
        :param cookie: cookie
        :return:
        '''
        br = BaseRequest()
        msg = br.run_main(method, url, data, cookie)
        # print(msg)
        return msg

    def cookie_option(self, cookie_opt, key=None):
        '''

        :param cookie_opt: 对应cookie操作
        :param key:比如 web和APP之类对应cookie.json的键
        :return:
        '''
        cookie_opt = cookie_opt
        hc = Handle_cookie()
        cookie_text = ''
        if cookie_opt == 'yes':
            cookie_text = hc.get_cookie_value(key)
        else:
            cookie_text = None
        return cookie_text

'''
-----------------------------------------9.16晚7点计划----------------------------------------------------------
1.把excel更新成一个列表嵌套字典的形式，简单来说就是废掉行数和列数的定位，采用字典键的定位-----OK
2.改造get_api_msg。
3.cookie的写入操作和header的操作
'''

if __name__ == '__main__':
    rm = RunMain()
    rm.run_case()

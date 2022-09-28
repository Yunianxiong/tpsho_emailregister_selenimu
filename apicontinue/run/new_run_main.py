# coding=utf-8
import json
import os
import sys

# 添加工程路径。防止找不到模块
import mock
import requests

base_path = os.getcwd()
sys.path.append(base_path)
from handle.read_excel import Read_Excel
from Base_request.base_requests import BaseRequest
from handle.handle_result import Hand_result
from handle.handle_cookie import Handle_cookie
from handle.handle_condition import Hadnle_codition
from handle.handleini import HandleInit

class RunMain:
    def __init__(self):
        self.re = Read_Excel()
        self.hi=HandleInit()

    def run_case(self,excel_data_dict):
        '''

        :param excel_data_dict_list:
        :return:
        '''
        #excel_data_dict_list = self.re.get_excel_dict_list()
        line_data_dict=excel_data_dict

        fin_result_num=int(self.hi.get_value('fin_result'))
        fail_response_num=int(self.hi.get_value('fail_response'))
        line_number = line_data_dict['line_number']
        case_number = line_data_dict['case_number']
        is_run = line_data_dict['is_run']
        before_condition = line_data_dict['before_condition']
        depend_key=line_data_dict['depend_key']
        link_url = line_data_dict['link_url']
        case_method = line_data_dict['case_method']
        case_data = json.loads(line_data_dict['case_data'])
        cookie_opt = line_data_dict['cookie_opt']
        header_opt = line_data_dict['header_opt']
        ex_result_method = line_data_dict['ex_result_method']
        ex_result = line_data_dict['ex_result']
        fin_result = line_data_dict['fin_result']
        fail_response = line_data_dict['fail_response']

        if before_condition:
            depend_data=self.get_depend_data(before_condition)
            case_data[depend_key]=depend_data
        cookie_text = self.cookie_option(cookie_opt, 'web',line_data_dict)
        api_msg = self.get_api_msg(case_method, link_url, case_data, cookie_text)
        if ex_result_method == 'mec':
            result_msg = self.get_handle_result_msg(ex_result_method, link_url, api_msg['errorCode'])
            #拿"errorCode": 1006和"errorDesc": "token error",前者先拿进get_handle_result_msg里面去获取
            #code_message.json相对应的信息-后者拿来和get_handle_result_msg返回来的信息进行比对
            if api_msg['errorDesc'] == result_msg:
                fin_result = '用例通过'
                print(f"这是第一次用例-->{fin_result}-->{api_msg['errorDesc']}和{result_msg}")
                self.re.write_excel(line_number, fin_result_num, fin_result)
            else:
                fin_result = '用例失败'
                self.re.write_excel(line_number, fin_result_num, fin_result)
                self.re.write_excel(line_number, fail_response_num, str(api_msg))
        #这个走excel的
        if ex_result_method == 'errorcode':
            # 这个是直接走excel的。
            if str(api_msg['errorCode']) == ex_result:
                fin_result = '用例通过'
                self.re.write_excel(line_number, fin_result_num, fin_result)
            else:
                fin_result = '用例失败'
                self.re.write_excel(line_number, fin_result_num, fin_result)
                self.re.write_excel(line_number, fail_response_num, str(api_msg))
        if ex_result_method == 'json':

            if api_msg['errorCode'] == '1000':
                # 对应result.json的两部分，一个成功，一个失败。分别获取两个字典比较是否为相应的json格式
                status_str = 'sucess'
            else:
                status_str = 'error'
            msg = self.get_handle_result_msg(ex_result_method, link_url, status_str, api_msg)
            # print(api_msg)
            if msg == True:
                fin_result = '用例通过'
                self.re.write_excel(line_number, fin_result_num, fin_result)
            else:
                fin_result = '用例失败'
                self.re.write_excel(line_number, fin_result_num, fin_result)
                self.re.write_excel(line_number, fail_response_num, str(api_msg))

        return fin_result

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

    def cookie_option(self, cookie_opt, key=None, url_dict=None):
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
        elif cookie_opt == 'write':
            #这个的问题是我不知道啥时候要写入cookie，而且cookie是request header那边获得的。这也是我比较懵的一点。所以暂时用自动返回文件替换
            #在返回的信息里面加入"cookie":{"addsdsd":"vjodkopsfkpokxpc"}---mock模拟一下
            '''            
            try:
                cookie_value=self.get_api_msg(method=url_dict['case_method'], url=url_dict['link_url'],
                                                data=url_dict['case_data']
                                                )['cookie']
                hc.write_cookie(key, cookie_value)
            except KeyError:
                print("cookie为空")
            
            '''
            cookie_value={"addsdsd": "vjodkopsfkpokxpc"}
            mm=mock.Mock(return_value=cookie_value)
            hc.write_cookie(key, mm())
            cookie_text = None
        elif cookie_opt == 'no':
            cookie_text = None
        return cookie_text

    def get_depend_data(self,condition):
        '''
        无具体需求，暂时写死
        :param condition:
        :return:
        '''
        hconiton=Hadnle_codition()
        data_dict = {

            "status": 0,
            "data": {
                "banner": [
                    {
                        "id":1001,
                        'password':1111123232
                    },
                    {
                        "id":2001,
                        "email":"dddd@qq.cc"
                    }
                ]

            }
        }
        pass_data = {
            'case': 'case_001',
            'tf_opt': 'no',
            'data_text': data_dict
        }
        res=hconiton.find_condition_data(condition,pass_data)
        return res



'''
-----------------------------------------笔记记录----------------------------------------------------------
1.把excel更新成一个列表嵌套字典的形式，简单来说就是废掉行数和列数的定位，采用字典键的定位-----OK
2.改造get_api_msg。-------------------------------------这个不用改--------------没做
3.cookie的写入操作和header的操作-------------------------------------------------暂无，没关系
4.前置条件依赖----前置case的输出作为本次case的输入。------------------------------这个暂时OK，因为数据写死了。
        前置条件这个--》视频中有两个方案 ：
        第一个是以上前置条件中case编号的输出为本次输入的参数之一：
            遇到问题：我把整个dictionary放进去jsonpath_rw没办法根据条件解析===》
                最好是知道前面case输出的格式--》明确要获取的值--》明确编写的条件-》这边暂时写死返回数据，进行模拟。
        第二个是将case进行先后循序的排序，然后将输出都放在excel表格进行获取
            第二个--》将case拆分，比如一个查询订单的接口，可以拆分成，创建订单，获取订单，更新订单，删除订单-然后一次获取信息
        
----------------------------------------疑问合集----------------------------------------------------------------
1.这个的问题是我不知道啥时候要写入cookie，而且cookie是request header那边获得的。这也是我比较懵的一点。
2.依赖条件：前置条件依赖----前置case的输出作为本次case的输入。我需要获取什么样的信息，怎么加入进去。

-----------------------------------------自9.17开始的报错记录-----------------------------------------------------
1.TypeError: '<' not supported between instances of 'str' and 'int'  ===》 fin_result_num=int(self.hi.get_value('fin_result'))
    这一行出错，配置表读取的类型是str,写入需要的是int。。
2.TypeError: string indices must be integers  -->    line_number = line_data_dict['line_number']
    new_run_main.runcase()沿用了原先的for循环，需要传参的是整个list，而ddt那边传参是list里面的单个字典元素。
3.ddt_case那边针对mec和errorcode类型的，fin_result输出为NONE，原因是最后的return没有取消缩进，在json类型下面。读取默认值NONE

'''

if __name__ == '__main__':
    rm = RunMain()
    excel_dict_list=rm.re.get_excel_dict_list()[0]
    res=rm.run_case(excel_dict_list)
    print(res)


    '''    
    urll='http://www.imooc.com/api3/getbanneradvertver2'
    url = 'api3/newcourseskill'
    data = {"username": "111111"}
    res=requests.get(urll,data).cookies.values()
    cookie_value=res
    print(cookie_value)
    
    '''

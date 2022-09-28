#coding=utf-8
import os
import sys
base_path=os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(base_path)
from mitmproxy import http
from handle.handle_json import HandeJson
hj=HandeJson()
class get_data:

    def request(self,flow):
        request_data=flow.request
        self.request_url=request_data.url
        request_pr=request_data.query
        #request_from=request_data.urlencoded_fowm
        print(f'url->{self.request_url}')
        print(f'pr->{request_pr}')
        print(f'data->{request_data}')


    def response(self,flow):
        if "imooc" in self.request_url:
            first_url=self.request_url.split('.com')
            if "?" in first_url[1]:
                two_url=first_url[1].split('?')
            else:
                two_url=first_url[1]
            return_data=hj.get_json_value('user_data',two_url)
            response_data=flow.response
            response_status_codes=response_data.status_code
            response_desc=response_data.text
            response_header=response_data.headers
            conten_type=response_header['content-type']
            response_data.set_text(return_data)
            if conten_type=='image/png':
                print('返回的是一个图片')
            elif conten_type=='application/json':
                print(f"status_codes-->{response_status_codes}")
                print(f"desc--->{response_desc}")
                print(f"header-->{response_header}")
                print(f"conten_type-->>{conten_type}")


addons=[
    get_data()
]
'''
mitmweb -s .\

 mitmweb -s .\mitmproxy_study.py

'''
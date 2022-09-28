#coding=utf-8

import logging
import os.path
import datetime
class Use_log(object):
    def __init__(self):
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    #创建流-控制台输出
        self.consle=logging.StreamHandler()
        '''        
        self.logger.addHandler(self.consle)
        self.logger.debug('dddd')
        '''

        #文件输出
        file_name=os.path.dirname(os.path.abspath(__file__))
        #print(file_name)
        file_n=os.path.join(file_name,'log_data')
        #print(file_n)
        now_time= datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        #print(now_time)
        log_name=file_n+'\\'+now_time
        #print(log_name)

        #添加，输出流
        fiel_handle=logging.FileHandler(filename=log_name,encoding='utf-8')
        fiel_handle.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s %(filename)s %(funcName)s  %(lineno)d %(levelno)s ---> %(message)s')
        fiel_handle.setFormatter(formatter)
        self.logger.addHandler(fiel_handle)


        #self.logger.debug('log_msg')


        #流关闭

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.consle.close()
        #移除流
        self.logger.removeHandler(self.consle)


if __name__=='__main__':
    ul=Use_log()
    lg=ul.get_log()
    lg.debug('dddd')
    ul.close_handle()

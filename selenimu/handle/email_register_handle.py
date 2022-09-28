#coding=utf-8

from page.email_register_page import Email_register
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from base.tm_checkcode import Get_check_code

class Email_register_handle(object):
    def __init__(self,driver):
        self.handle_element=Email_register(driver)
        self.hadle_check_code=Get_check_code(driver,check_element=self.handle_element.get_image_code_element())

    def send_email_value(self,value):
        self.handle_element.get_email_element().send_keys(value)

    def send_password_value(self,value):
        self.handle_element.get_password_element().send_keys(value)

    def send_password_again_value(self,value):
        self.handle_element.get_password_again_element().send_keys(value)

    def send_rec_tel_value(self,value):
        self.handle_element.get_rec_tel_element().send_keys(value)

    def send_check_code_value(self,value):
        self.handle_element.get_check_code_element().send_keys(value)

    #调用dddcor去识别验证码
    def get_check_code_value(self):
        text=self.hadle_check_code.get_code_run2()
        return text

    #协议勾选-一般默认勾选
    def chick_check_text(self):
        self.handle_element.get_check_text_element().click()

    #获取弹窗文本
    def get_pop_text(self):
        try:
            pop_text=self.handle_element.get_error_pop_element().text
        except:
            pop_text=None
        return pop_text

    #点击弹窗确定按钮
    def click_pop(self):
        self.handle_element.get_error_pop_button_element().click()

    #确认是否有错误弹窗
    def check_password_pop(self):
        check_pop=self.handle_element.get_user_password_pop_element()
        check_pop_tf = ec.visibility_of_element_located(check_pop)
        return check_pop_tf

    #关闭密码错误弹窗
    def check_password_pop_exit(self):
        self.handle_element.get_user_password_pop_exit_element().click()

    #注册
    def register_button_click(self):
        self.handle_element.click_register_button().click()


#仅用于测试是否可运行
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://192.168.50.131/Home/User/reg/t/email.html")
    erh=Email_register_handle(driver)
    erh.send_email_value('123456@tis.com')
    driver.close()

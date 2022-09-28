#coding=utf-8

from base.find_el import Find_element
from selenium import webdriver

class Email_register(object):

    #传入driver调用Find_element
    def __init__(self,driver):
        self.get_el_er=Find_element(driver=driver)

    def get_email_element(self):
        use_email=self.get_el_er.find_el('useemail')
        return use_email

    def get_password_element(self):
        use_password=self.get_el_er.find_el('usepass')
        return use_password

    def get_password_again_element(self):
        use_password_again=self.get_el_er.find_el('usepaasagin')
        return use_password_again

    def get_rec_tel_element(self):
        use_rec_tcl=self.get_el_er.find_el('userestel')
        return use_rec_tcl

    def get_check_code_element(self):
        check_code=self.get_el_er.find_el('checkcode')
        return check_code

    def get_image_code_element(self):
        image_code=self.get_el_er.find_el('imagecode')
        return image_code

    #信息错误弹窗
    def get_user_password_pop_element(self):
        password_pop=self.get_el_er.find_el('useepc')
        return password_pop

    #信息错误弹窗关闭元素
    def get_user_password_pop_exit_element(self):
        password_pop_exit=self.get_el_er.find_el('useepx')
        return password_pop_exit

    #弹窗信息获取
    def get_error_pop_element(self):
        error_pop=self.get_el_er.find_el('errormsg')
        return error_pop

    #弹窗信息确定按钮
    def get_error_pop_button_element(self):
        error_pop_button=self.get_el_er.find_el('errorbutton')
        return error_pop_button

    #勾选信息
    def get_check_text_element(self):
        check_text_element=self.get_el_er.find_el('usecheck')
        return check_text_element

    def click_register_button(self):
        register_button=self.get_el_er.find_el('registerbutton')
        return register_button

#仅用于测试是否正常运行
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://192.168.50.131/Home/User/reg/t/email.html")
    erp=Email_register(driver)
    var=erp.get_email_element()
    print(var)
    driver.close()

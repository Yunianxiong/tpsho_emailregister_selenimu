#coding=utf-8
import time

from handle.email_register_handle import Email_register_handle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Email_register_bussiness(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)
        self.emali_register=Email_register_handle(driver=self.driver)

    def get_driver(self,url):
        #option=webdriver.ChromeOptions()
        #option.add_experimental_option("detach",True)
        service = Service(executable_path=r"C:\Users\yuxiaonian\AppData\Local\Google\Chrome\Application\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get(url=url)
        driver.maximize_window()
        time.sleep(5)
        return driver

    def email_login(self,email_value,password_value,password_again_value,
                    use_rec_tel_value,check_code='1111'
                    ):
        try:
            self.emali_register.send_email_value(email_value)
            self.emali_register.send_password_value(password_value)
            self.emali_register.send_password_again_value(password_again_value)
            self.emali_register.send_rec_tel_value(use_rec_tel_value)
            check_code = self.emali_register.get_check_code_value()
            self.emali_register.send_check_code_value(check_code)
            self.emali_register.register_button_click()

        except:
            pass

        finally:
            judge_text=''
            if self.error_pop_judge():
                judge_text=self.emali_register.get_pop_text()
            else:
                judge_text='通过'
            return judge_text





    def error_msg_judge(self):

        error_text=''
        error_msg=self.emali_register.get_pop_text()
        if error_msg=='请输入正确邮箱':
            error_text='邮箱错误'
        elif error_msg=='图像验证码错误':
            error_text='验证码错误'
        elif error_msg=='密码有效长度为6-16位!':
            error_text='初次密码输入错误'
        elif error_msg=='两次密码不一致':
            error_text='再次输入密码错误'
        elif error_msg=='请认真阅读并勾选服务协议!':
            error_text='未勾选协议'
        else:
            error_text='有问题'
        return error_text


    #判断弹窗
    def error_pop_judge(self):
        error_pop_tf=self.emali_register.check_password_pop()
        return error_pop_tf


    def driver_close(self):
        self.driver.quit()






if __name__=='__main__':
    url="http://192.168.50.131/Home/User/reg/t/email.html"
    erb=Email_register_bussiness(url)
    text=erb.email_login('123','123456789','123456789','987654321')
    print(text)
    time.sleep(10)
    erb.driver_close()
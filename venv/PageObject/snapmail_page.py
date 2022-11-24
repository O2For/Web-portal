from poium import Page,Element
from PageObject.message_template_page import Template

import time
import os
class MailBox(Page):
    '''邮箱的各种操作，目前只有关于snapmail的'''


    def open_Mail(self):
        '''打开邮箱'''
        #new_window = 'window.open("{}")'.format('https://www.snapmail.cc/#/')  # js函数，此方法适用于所有的浏览器
        new_window = 'window.open("{}")'.format('https://www.8164.cc/#/addEmailBox')
        self.execute_script(new_window);
        time.sleep(3)

        self.switch_to_window(1)


    #def create_new_email(self,email):
    def create_new_email(self,*email):
        '''像snapmail中添加一个新的邮箱'''
        time.sleep(3)
        Element(xpath="//i[@class='el-icon-plus']",describe="add",timeout=3).click()
        Element(xpath="//input[@class='el-input__inner']", timeout=2).clear()
        Element(class_name="el-input__inner", timeout=2).send_keys(email)
        #Element(xpath="//button[@ng-click='addEmailBox()']",timeout=2, describe="save").click();time.sleep(3)
        Element(xpath="//button").click();time.sleep(20)

    def email_type_call(self,email,type):
        '''调用邮箱的各种函数集合'''

        email_type={
            0 : 'register_valid8Me',#打开v8 发送的注册邮箱手机端客户端验证码
            1 : 'connect_valid8Me'  #打开受邀请的注册邮箱链接，受邀请的用户 页面跳转到注册页面 且返回注册的用户邮箱
        }

        call=getattr(MailBox,email_type[type])# 等价于Mailbox.register_valid8Me()的继承
        call_black=call(self,email=email)#等价于Mailbox.register_valid8Me(self,email)
        return call_black





    def register_valid8Me(self,email):
        #打开 由v8发过来的注册邮箱


        #email_path='//span/span[contains(text(),"{}")]'.format(email);
        email_path = '//li/span[contains(text(),"{}")]'.format(email);
        print(email_path)
        Element(xpath=email_path,index=0).double_click();time.sleep(10)

        #Element(xpath='//span[contains(text(),"Request to Register with valid8Me")]').click() snapmail
        Element(xpath="//div[contains(text(),'Request to Register with valid8Me')]").click()
        time.sleep(10)
        return Template.Email_verification_code(self)

    def connect_valid8Me(self,email):
        email_path = '//li/span[contains(text(),"{}")]'.format(email);
        #Element(xpath=email_path).click();time.sleep(5)
        #Element(xpath='//span[contains(text(),"connect with you on valid8Me")]').click();
        Element(xpath="//div[contains(text(),'connect with you on valid8Me')]").click()
        #time.sleep(2)

        return Template.Email_verification_connction(self)









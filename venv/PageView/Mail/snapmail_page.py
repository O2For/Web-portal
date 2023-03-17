from poium import Page,Element
from PageView.Mail.message_template_page import Template

import time


class MailBox(Page):
    '''邮箱的各种操作，目前只有关于snapmail的'''

    def open_Mail(self):
        '''打开邮箱'''
        #new_window = 'window.open("{}")'.format('https://www.snapmail.cc/#/')  # js函数，此方法适用于所有的浏览器
        new_window = 'window.open("{}")'.format('https://snapmail.cc/#/addEmailBox')
        self.execute_script(new_window);
        time.sleep(5)

        self.switch_to_window(1)


    #def create_new_email(self,email):
    def create_new_email(self,*email):
        '''像snapmail中添加一个新的邮箱'''
        time.sleep(3)
        #添加邮箱
        Element(xpath="//a[@class='email-item ']",describe='+').click()
        Element(id_="inputEmail",describe="add input",timeout=3).click()
        Element(id_="inputEmail", timeout=2).clear()
        Element(id_="inputEmail", timeout=2).send_keys(email)
        #Element(xpath="//button[@ng-click='addEmailBox()']",timeout=2, describe="save").click();time.sleep(3)
        Element(xpath="//button[@class='btn btn-primary ng-binding']").click();


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
        '''type=0'''
        #打开 由v8发过来的注册邮箱
        email_path = '//span[contains(text(),"{}")]'.format(email);
        print(email_path)
        Element(xpath=email_path,index=0).double_click()
        self.wait_page_load_timeout(10)
        Element(xpath="//span[contains(text(),'Request to Register with valid8Me')]",timeout=10).click()



        return Template.Email_verification_code(self)

    def connect_valid8Me(self,email):
        ''' type = 1 : 'connect_valid8Me' '''

        email_path = '//span[contains(text(),"{}")]'.format(email);
        Element(xpath=email_path, index=0).double_click()
        Element(xpath="//span[contains(text(),'connect with you on valid8Me')]",timeout=10).click()
        self.wait_page_load_timeout(10)


        return Template.Email_verification_connction(self)









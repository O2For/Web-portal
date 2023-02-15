from poium import Page,Element
import re
import time

class Template(Page):
    '''关于邮件模板的相关函数'''

    def Email_verification_code(self):
        '''得到v8的验证码'''
        time.sleep(2)
        #self.switch_to_frame(1)
        message_text=Element(xpath="//tbody/tr/td/div/p").get_attribute('textContent')
        code = re.findall("\d+",message_text) # 正则化 提取数字
        return code[1]
    def Email_verification_connction(self):
        '''验证邮箱是否能够正常收到connction信息 以及
        The user use email link to customer portal'''

        time.sleep(15)
        #self.switch_to_frame(1);time.sleep(3)
        #message_text = Element(xpath="//tbody/tr/td/div/p",index=0).get_attribute('textContent')
        valid8me_link = Element(xpath='//tr/td/a', index=2)
        valid8me_link.click_and_ctrl();time.sleep(10)
        self.switch_to_window(1);time.sleep(5)

        mail_reture=Element(id_='register-email-field').get_attribute('value');
        #返回link过来的客户邮箱地址
        return mail_reture





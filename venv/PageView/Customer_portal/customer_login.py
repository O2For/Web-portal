from selenium.webdriver.common.keys import Keys
from PageView.Customer_portal.customer_system_page import *
from poium.common import logging
import time


class customer_login_page(Page):

    '这里是 Customer protal 的 login 和注册页面以及Home page的页面 基础定位'


    '''Sign in to valid8Me 页面的相关定位'''
    Email_Input = Element(xpath="//input[@placeholder='Enter your email']",describe="输入邮箱")
    Password = Element(xpath="//input[@placeholder='Enter password']",describe="password")
    Login =Element(xpath="//span[contains(text(),'Login')]",describe="login button")
    sign_up = Element(xpath="//span[contains(text(),'Sign Up')]",describe="sign up button")
    forgot_password =Element(xpath="//a[contains(text(),'Forgot')]")

    register_email_field = Element(id_='register-email-field',describe='注册页面输入邮箱')
    register_password_field = Element(id_='register-password-field',describe='注册页面输入密码')
    register_passwordRepeat_field = Element(id_='register-passwordRepeat-field',describe='注册页面输入确认密码')
    accept_read = Element(xpath="//a[contains(text(),'END USER-TERMS & CONDITIONS')]/preceding-sibling::label/*[1]")
    register_confirm_button = Element(id_='register-confirm-button')
    #code
    code_input = Element(xpath="//input[@placeholder='Please enter the code you received']", describe="验证码")
    confirm_btu = Element(xpath="//BUTTON/span[contains(text(),'Confirm')]", timeout=3, describe="code confirm button")
    #reole coprorate
    register_select_type_corporate = Element(id_='register-select-type-corporate')
    register_profile_corporate_confirm_button = Element(id_='handleLoginButton')
    legalName = Element(id_='register-profile-legalName-field')
    tradingName = Element(id_='register-profile-tradingName-field')




    inp_password = Element(xpath="//input[@placeholder='Please enter your password']", describe="password")
    '''St 094 95'''

    ##
    terms = Element(id_="register-showDialog-btn",describe="协议")
    terms_title = Element(xpath="//div[@class='title']")



        #reole

    ##########################################################
    register_select_type_individual=Element(id_='register-select-type-individual')
    register_profile_individual_confirm_button = Element(id_='register-profile-individual-confirm-button')
###################################################################
    '''St 094'''
    firstName=Element(id_='register-profile-firstName-field')
    lastName=Element(id_='register-profile-lastName-field')

    def SignUpCorp(self,Username,):
        self.register_confirm_button.click()
        self.code_input.send_keys(666666)
        self.confirm_btu.click()
        self.register_select_type_corporate.click()
        self.legalName.send_keys(Username)
        self.tradingName.send_keys(Username)
        self.register_profile_corporate_confirm_button.click()
        self.wait_page_load_timeout(5)
        time.sleep(5)

    def FirstSignCorp(self,Invite_email,Password,Username):
        '''前提用户已经被邀请 无需选择用户类型'''
        self.sign_up.click()
        self.register_email_field.send_keys(Invite_email)
        self.register_password_field.send_keys(Password)
        self.register_passwordRepeat_field.send_keys(Password)
        self.accept_read.click()
        self.register_confirm_button.click()

    def Login_step(self,Email,Password):
        self.wait_page_load_timeout(10)
        self.Email_Input.send_keys(Email)
        self.Password.send_keys(Password)
        self.Login.click()
        self.sleep(5)










class CustomerHomePage(Page):
    'Homepage 的相关操作'
    IdList=[]

    def _verfiy_Profile_SetUp(self):
        ''

        Element(id_='setName-modal-handleItemClick-btn21881')
        Element(id_='setName-modal-handleItemClick-btn21882')
        Element(id_='setName-modal-handleItemClick-btn21883')


    def closeProfile_SetUp(self):
        '关闭customer portal的任务栏弹窗'
        self.wait(5)

        Element(id_='setName-modal-dont-ask-checkbox').click()
        Element(id_='setName-modal-skip-button').click()
        self.sleep(3)



    def complete_your_Corporate_Identity(self,Jurisdiction,Number,
                                         Type,Date,Address):
        '完成 公司用户的基础操作 Action - complete_your_Corporate_Identity'
        Element(xpath='//div[contains(text(),"Complete your Corporate Identity")]',timeout=3).\
            click()
        IdList = ['ActionType7-CYCI-Jurisdiction-select','ActionType7-CYCI-companyType-select']
        for i in range(2):
            js='document.getElementById("{}").removeAttribute("readonly");'.\
            format(IdList[i])
            self.execute_script(js)#解除 ready only
        Element(id_=IdList[0]).send_keys(Jurisdiction)
        Element(id_='ActionType7-CYCI-Jurisdiction-select-option81').click()
        Element(id_=IdList[1]).click()
        Element(id_='ActionType7-CYCI-companyType-select-option4').click()
        Element(id_='ActionType7-CYCI-companyNumber-input').send_keys(Number)
        Element(id_='ActionType7-CYCI-dateOfIncorporation-datepicker').send_keys(Date)
        Element(id_='ActionType7-CYCI-officialAddress-input').send_keys(Address)
        TradingName = Element(id_='ActionType7-CYCI-tradingName-input'). \
            get_attribute('value')
        Element(id_='ActionType7-CYCI-complete-button',timeout=3).click()
        time.sleep(3)
        return TradingName

    def upload_company_logo(self,logo):
        '''Action upload company logo'''
        Element(xpath='//div[contains(text(),"Upload your company Logo")]').click()
        Element(xpath='//div/input').send_keys(logo);time.sleep(3)
        Element(id_='ActionType7-UYCL-confirm-button').click()
        Element(xpath='//span[contains(text(),"Yes")]').click();time.sleep(3)

    def Logout(self):
        Element(id_='navbar-handleAvatarClick-btn').click()
        Element(xpath="//div[contains(text(),'Logout')]").click();time.sleep(3)
        assert Element(id_="login-button").is_displayed()
        logging.info(f'Logout success')


    def jumppage_System(self):
        '''POFILE'''
        Element(id_='sidebar-menu-item-one').click();time.sleep(1)

class RecentShares(Page):
    view_all=Element(id_='hompage-viaw-all-button')

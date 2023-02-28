from poium import Page,Element
from Base.base import InvalidElementException
from PageView.customer_system_page import *
from selenium import webdriver
import allure

import time


class customer_login_page(Page):

    '这里是 Customer protal 的 login 和注册页面以及Home page的页面 基础定位'

    email = Element(xpath="//input[@placeholder='Enter your email']",describe="输入邮箱")
    password = Element(xpath="//input[@placeholder='Enter password']",describe="password")
    login =Element(xpath="//span[contains(text(),'Login')]",describe="login button")
    sign_up = Element(xpath="//span[contains(text(),'Sign Up')]",describe="sign up button")
    forgot_password =Element(xpath="//a[contains(text(),'Forgot')]")
    login_button = Element(id_='login-button')




    inp_password = Element(xpath="//input[@placeholder='Please enter your password']", describe="password")
    register_email_field =Element(id_='register-email-field')
    register_password_field=Element(id_='register-password-field')
    register_passwordRepeat_field=Element(id_='register-passwordRepeat-field')
    ##
    accept_read = Element(xpath="//a[contains(text(),'END USER-TERMS & CONDITIONS')]/preceding-sibling::label/*[1]")
    terms = Element(id_="register-showDialog-btn",describe="协议")
    terms_title = Element(xpath="//div[@class='title']")

    register_confirm_button=Element(id_='register-confirm-button')

    code_input =  Element(xpath="//input[@placeholder='Please enter the code you received']",describe="验证码")
    confirm_btu = Element(xpath="//BUTTON/span[contains(text(),'Confirm')]", timeout=3,describe="code confirm button")
    #reole
    register_select_type_corporate=Element(id_='register-select-type-corporate')
    register_profile_corporate_confirm_button=Element(id_='register-profile-corporate-confirm-button')
    legalName=Element(id_='register-profile-legalName-field')
    tradingName=Element(id_='register-profile-tradingName-field')
    ##########################################################
    register_select_type_individual=Element(id_='register-select-type-individual')
    register_profile_individual_confirm_button = Element(id_='register-profile-individual-confirm-button')

    firstName=Element(id_='register-profile-firstName-field')
    lastName=Element(id_='register-profile-lastName-field')

class CustomerHomePage(Page):
    'Homepage 的相关操作'
    IdList=[]

    def _verfiy_Profile_SetUp(self):
        ''
        try:
            Element(id_='setName-modal-handleItemClick-btn21881')
            Element(id_='setName-modal-handleItemClick-btn21882')
            Element(id_='setName-modal-handleItemClick-btn21883')
        except :

            raise InvalidElementException("No Find this Element in page")

    def closeProfile_SetUp(self):
        '关闭customer portal的任务栏弹窗'

        Element(id_='setName-modal-dont-ask-checkbox').click()
        Element(id_='setName-modal-skip-button').click()



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

    def logout(self):
        Element(id_='navbar-handleAvatarClick-btn').click()
        Element(id_='header-logout-btn').click();time.sleep(3)

    def jumppage_System(self):
        '''POFILE'''
        Element(id_='sidebar-menu-item-one').click();time.sleep(1)

class RecentShares(Page):
    view_all=Element(id_='hompage-viaw-all-button')


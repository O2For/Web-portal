from selenium.webdriver.common.keys import Keys
from PageView.Customer_portal.customer_system_page import *
from poium.common import logging
import time

'''登陆页面的相关操作'''
class customer_login_page(Page):
    '''登陆页面的相关操作'''

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
    confirm_btu = Element(id_='register-code-validation-confirm-button', timeout=3, describe="code confirm button")
    #reole coprorate
    register_select_type_corporate = Element(id_='register-select-type-corporate')
    register_select_type_individual = Element(id_='register-select-type-individual')
    register_profile_corporate_confirm_button = Element(xpath="//button/span[contains(text(),'Confirm')]",index=0)

    confirm_ind_name_but=Element(xpath="//button/span[contains(text(),'Confirm')]",index=0)

    legalName = Element(id_='register-profile-legalName-field')
    tradingName = Element(id_='register-profile-tradingName-field')




    inp_password = Element(xpath="//input[@placeholder='Please enter your password']", describe="password")
    '''St 094 95'''

    ##
    terms = Element(id_="register-showDialog-btn",describe="协议")
    terms_title = Element(xpath="//div[@class='title']")


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

    def SignUpInd(self,Username):
        self.register_confirm_button.click()
        self.code_input.send_keys(666666)
        self.confirm_btu.click()
        self.register_select_type_individual.click()
        self.firstName.send_keys(Username)
        self.lastName.send_keys(Username);self.sleep(1)
        self.confirm_ind_name_but.click()
        self.wait_page_load_timeout(5)
        time.sleep(5)

    def FirstSignCorp(self,Invite_email,Password,Username):
        '''前提用户已经被邀请 无需选择用户类型'''
        self.sign_up.click()
        self.register_email_field.send_keys(Invite_email)
        self.register_password_field.send_keys(Password)
        self.register_passwordRepeat_field.send_keys(Password)
        self.accept_read.click()
        self.code_input.send_keys('666666')
        self.confirm_btu.click(); self.sleep(3)
        self.register_confirm_button.click()
        self.legalName.send_keys(Username)
        self.tradingName.send_keys(Username)
        self.register_profile_corporate_confirm_button.click();self.sleep(3)



    def FirstSignInd(self,Invite_email,Password,Username):
        '''前提用户已经被邀请 无需选择用户类型'''
        self.sign_up.click()
        self.register_email_field.send_keys(Invite_email)
        self.register_password_field.send_keys(Password)
        self.register_passwordRepeat_field.send_keys(Password)
        self.accept_read.click()
        self.register_confirm_button.click()
        self.code_input.send_keys('666666')
        self.confirm_btu.click(); self.sleep(3)
        self.firstName.send_keys(Username)
        self.lastName.send_keys(Username); self.sleep(1)
        self.confirm_ind_name_but.click();self.sleep(3)

    def Login_step(self,Email,Password):
        """
        直接登录脚本
        :param Email:
        :param Password:
        :return:
        """
        self.wait_page_load_timeout(10)
        self.Email_Input.send_keys(Email)
        self.Password.send_keys(Password)
        self.Login.click()
        self.sleep(5)



'''Homepage 的相关操作'''
class CustomerHomePage(Page):
    'Homepage 的相关操作'
    IdList=[]
    _upload_iconClass = 'uploadCard'

    '传送 在Home 页面上传文档,一次传送一个文件类型'
    def UploadDocHome_Corp(self,DocPath,dataTest,Doc_type):
        '在Home 页面上传文档,一次传送一个文件类型'

        _docTypeId = 'document-upload-modal-docVault-select'
        _docName = '//li/span[contains(text(),"{}")]'.format(Doc_type)
        _confirmUploadDocHomeList = "//p[contains(text(),'{}')]".format(Doc_type)

        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径

        DocList_AddDateOfIssue = ['Filed Corporate Accounts','Company Ownership Structure',
                                  'Test for Corp1','Test for Corp2']
        OrtherInfor=['Test for Corp1']

        Element(class_name=self._upload_iconClass).click()
        Element(id_=_docTypeId,describe='点击上传文件的下拉框',index=0).click()
        Element(xpath=_docName, describe='点击下拉列表中需要上传的文件').click()
        Element(xpath="//em/following-sibling::input").send_keys(DOCPATH + AllDoc[Doc_type]);time.sleep(2)

        if Doc_type in DocList_AddDateOfIssue:

            Element(xpath="//label[contains(text(),'Date of Issue')]/..//input",describe='Date of Issue').send_keys('01/01/1999')
            if Doc_type not in OrtherInfor:
                pass
            else:
                Element(id_='document-upload-modal-input-doc',describe='input copr name doc need').send_keys('Other')
        else:
            pass

        Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();time.sleep(3)
        assert Element(xpath=_confirmUploadDocHomeList)

        logging.info(f"Type is :{Doc_type}-> upload successfully")


    '传送 在Home 页面上传文档,一次传送一个文件类型'
    def UploadDocHome_Ind(self,DocPath,dataTest,Doc_type,username):


        _docTypeId = 'document-upload-docVault-select'
        _docName = '//li/span[contains(text(),"{}")]'.format(Doc_type)
        _confirmUploadDocHomeList = "//p[contains(text(),'{}')]".format(Doc_type)

        DOCPATH = DocPath  # 跟目录
        AllDoc = dataTest  # 路径

        DocList_AddDateOfIssue = ['Certified Document', 'Utility Bill', 'Bank / Financial Statement',
                                  'Test for Ind1', 'Current Bank Account Statement', 'Current Mortgage Statements',
                                  'Current Credit Union Statement', 'Current Loan Statements', 'Supplier Statements',
                                  'Current Social Welfare Payslips', 'Employment earnings summary',
                                  'Share Certificates or Annual Statements']
        cur_date = time.strftime("%d/%m/%Y")
        self.sleep(4)

        Element(class_name=self._upload_iconClass).click()
        Element(id_=_docTypeId,describe='点击上传文档下拉框',index=0).click()
        Element(xpath=_docName).click()
        Element(xpath="//em/following-sibling::input").send_keys(DOCPATH + AllDoc[Doc_type]);time.sleep(2)

        if Doc_type=='Passport':

            Element(id_='document-upload-local-doc-submit-button', describe='submit', timeout=3).click();self.sleep(5)#等待regular
            Element(id_='document-upload-regular-inputList-item-not-513',describe='#修改到期时间').send_keys(cur_date,clear=True)
            Element(id_='document-upload-regular-inputList-item-not-514',describe='#修改 出生时间').send_keys('01/01/1999',clear=True)
            Element(id_='document-upload-regular-inputList-item-not-518').send_keys(username, clear=True)
            Element(id_='document-upload-regular-inputList-item-not-517').clear()
            Element(xpath="//BUTTON/span[contains(text(),'Confirm')]",describe='# 确认regular 证件识别结果').click();self.sleep(5)
            if Element(xpath="//span[contains(text(),'Update Profile Details?')]",index=1).is_exist():
                Element(xpath="//span[contains(text(),'Yes, I would')]",index=1).click();
            else:
                pass
        else:
            if Doc_type == 'National ID Card':

                Element(xpath="//label[contains(text(),'Date of Expiry')]/..//input", describe='Date of Expiry').send_keys(
                    cur_date)
            elif Doc_type in DocList_AddDateOfIssue:

                Element(xpath="//label[contains(text(),'Date of Issue')]/..//input", describe='Date of Issue').send_keys(
                    '01/01/1999')
            else:
                pass

            Element(id_='document-upload-local-doc-submit-button', describe='提交文档', timeout=3).click();time.sleep(5)
        assert Element(xpath=_confirmUploadDocHomeList,describe='验证上传的文档是否出现在列表中')
        logging.info(f"Type is :{Doc_type}-> upload successfully")
        return

    '获取 文件最新的版本号码'
    def GetDoclatestVersion(self,Doc_type):
        """

        :param Doc_type:
        :return: 得到最新的文件版本号码
        """
        _docPhotoX='//p[contains(text(),"{}")]/../../../preceding-sibling::div'.format(Doc_type)
        _version = 'document-view-modal-select'
        _closeButtonClass = 'el-dialog__close'
        Element(xpath = _docPhotoX).click();self.sleep(3)
        DoclatestVersion = Element(id_ = _version).get_attribute('value')
        Element(class_name= _closeButtonClass,index=0).click()

        return DoclatestVersion


    '关闭弹出窗口'
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


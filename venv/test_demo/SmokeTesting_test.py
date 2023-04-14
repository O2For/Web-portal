import os
import sys
from time import sleep
import pytest
import allure
from pytest_assume.plugin import assume

#POB

sys.path.append(os.getcwd())
from PageView.Customer_portal.customer_login import *
from PageView.Customer_portal.customer_system_page import *
from PageView.Business_portal.business_login import LoginPage
from PageView.Business_portal.MyWorkPage import *

from PageView.Customer_portal.customer_connections_companies_page import *
from PageView.Customer_portal.customer_connections_corpRep_page import *
from PageView.Customer_portal.Documents.customer_corporateDoc_page import *
from PageView.Customer_portal.customer_connections_AuthorisedRep import *
from PageView.Customer_portal.customer_document_page import *
from PageView.Customer_portal.customer_action_page import *
from PageView.Business_portal.Configuration.Product_services import *
from Common.config import *
#

# 数据准备导入路径
from Data.test_data import GetData

''' 当前路径(使用 abspath 方法可通过dos窗口执行)'''
current_path = os.path.dirname(os.path.abspath(__file__))
print("当前路径"+current_path)


'''得到本次测试配置数据：'''
sys.path.append(os.getcwd())
data=GetData.TestData()


'''得到本次导入到测试中的excel数据：'''
FileExecl=FileOperation()
Test_data=FileExecl.getExecl()


@allure.epic('Somke Testing Valid8Me v2.11.0')
class TestCaes:

    #@allure.feature('Verify that the corporate user could be set up successfully.')
# ------------------------------------------------------------------------------------------------#
    @allure.severity("blocker")
    @pytest.mark.skip('copr 跳过')
    @pytest.mark.parametrize("terms_title,reg__corp_email,Email_type,reg_pwd,mailbox,legalName,tradingName",
                             [("End user-terms",
                               data.corp_inf.corp_email,
                               data.Email_type.snapmail,
                               data.corp_inf.password,
                               data.Env.test_mail,
                               data.corp_inf.corp_email,
                               data.corp_inf.TN
                               )])

    @allure.story('Verify that the corporate user could be set up successfully.')
    def test_St089(self,drivers,
                   terms_title,reg__corp_email,Email_type,reg_pwd,mailbox,legalName,tradingName):
        page = customer_login_page(drivers)

        with allure.step('You should then read and accept the terms'
                         ' and conditions if you are happy with them.'):
            with allure.step('Open Valid8me customer portal'):
                page.open(data.Env.url_cur_qa)
                #page.execute_script("document.body.style.transform='scale(0.5)'")
                #zoom_out = "document.body.style.zoom='0.5'"
                #page.execute_script(zoom_out)

                page.sign_up.click();sleep(2)
                # with allure.step('Read and accept the terms'):
                #     page.terms.click()
                #     #
                #     page.switch_to_window(1)
                #     #with assume: assert terms_title in page.terms_title.get_attribute('textContent'),'没有条款'
                #     #page.accept_read.click()
        with allure.step('You will have to enter your email address '
                         'and password and confirm this password.'):
            #page.switch_to_window(0)
            # with allure.step('Check confirm button is_disenabled without infer'):
            #     with assume: assert not page.register_confirm_button.click()
            with allure.step('Input email & password & confirm password'):
                page.register_email_field.send_keys(reg__corp_email+Email_type)
                page.register_password_field.send_keys(reg_pwd)
                page.register_passwordRepeat_field.send_keys(reg_pwd)
                page.accept_read.click();sleep(1)
                page.register_confirm_button.click();sleep(1)
        with allure.step('You will then receive a one-time code (OTC) '
                         'to your email, please enter this into the screen, '
                         'you will have a limited time to do so.'):
            with allure.step('Check mailbox'):

                #new_window = 'window.open("{}")'.format(mailbox)  # js函数，此方法适用于所有的浏览器
                #page.execute_script(new_window);sleep(3)

                #page.switch_to_window(2)
                Mailbox=MailBox(drivers) # 调用脚本
                Mailbox.open_Mail()
                MailBox.create_new_email(reg__corp_email)
                #Mailbox.create_new_email(reg__corp_email);sleep(3)
            with allure.step('Receive a one-time code (OTC)'):

                verify_code=Mailbox.email_type_call(reg__corp_email+Email_type,0)
                page.switch_to_window(0);sleep(3)
                page.code_input.send_keys(verify_code);sleep(3)
            with allure.step('Please enter this into the screen,'):
                page.confirm_btu.click();sleep(1)
        with allure.step('You can select corporate in register page'):
            with allure.step('Select corporate'):
                page.register_select_type_corporate.click()
        with allure.step('You must input you Legal name and Trading name so you can Next'):
            page.register_profile_corporate_confirm_button.click()
            assert page.legalName.is_enabled()
            page.legalName.send_keys(legalName);page.tradingName.send_keys(tradingName)
            page.register_profile_corporate_confirm_button.click();sleep(3)

# ------------------------------------------------------------------------------------------------#

    @pytest.mark.parametrize("terms_title,Email_type,reg_pwd,mailbox_url,reg_ind_email,FN,LN",
                             [("End user-terms",
                               data.Email_type.snapmail,
                               data.corp_inf.password,
                               data.Env.test_mail,
                               data.ind_inf.ind_email,
                               data.ind_inf.FN,
                               data.ind_inf.LN
                               )])
    @allure.story('When setting up a individual account:')
    @pytest.mark.skip('indivdual 跳过')
    def test_St090(self,drivers,
                   terms_title,reg_ind_email,Email_type,reg_pwd,mailbox_url,FN,LN):
        page = customer_login_page(drivers)
        with allure.step('You should then read and accept the terms'
                         ' and conditions if you are happy with them.'):
            with allure.step('Open Valid8me customer portal'):
                page.open(data.Env.url_cur_qa)
                page.sign_up.click();
                sleep(2)
                with allure.step('Read and accept the terms'):
                    page.terms.click()
                    #
                    page.switch_to_window(1)
                    with assume: assert terms_title in page.terms_title.get_attribute('textContent')
                    # page.accept_read.click()
        with allure.step('You will have to enter your email address '
                         'and password and confirm this password.'):
            page.switch_to_window(0)
            with allure.step('Check confirm button is_disenabled without infer'):
                with assume: assert not page.register_confirm_button.click()
            with allure.step('Input email & password & confirm password'):
                page.register_email_field.send_keys(reg_ind_email + Email_type)
                page.register_password_field.send_keys(reg_pwd)
                page.register_passwordRepeat_field.send_keys(reg_pwd)
                page.accept_read.click()
                page.register_confirm_button.click();
                sleep(1)
        with allure.step('You will then receive a one-time code (OTC) '
                         'to your email, please enter this into the screen, '
                         'you will have a limited time to do so.'):
            with allure.step('Check mailbox'):
                new_window = 'window.open("{}")'.format(mailbox_url)  # js函数，此方法适用于所有的浏览器
                page.execute_script(new_window);
                sleep(3)

                page.switch_to_window(2)
                Mailbox = MailBox(drivers)  # 调用脚本
                Mailbox.create_new_email(reg_ind_email);
                sleep(3)
            with allure.step('Receive a one-time code (OTC)'):
                verify_code = Mailbox.check_latest_messages(reg_ind_email + Email_type) #
                #通过邮件查看 最新的code码
                page.switch_to_window(0);
                sleep(3)
                page.code_input.send_keys(verify_code);
                sleep(3)
            with allure.step('Please enter this into the screen,'):
                page.confirm_btu.click();
                sleep(1)
        with allure.step('You can select individual in register page'):
            with allure.step('Select corporate'):
                page.register_select_type_individual.click()

        with allure.step('You must input you First name and Last name so you can Next'):
            page.register_profile_individual_confirm_button.click()
            assert page.legalName.is_enabled()
            page.firstName.send_keys(FN);page.lastName.send_keys(LN)
            page.register_profile_individual_confirm_button.click();sleep(3)

    @pytest.mark.parametrize("tradingName,Jurisdiction,Number,Company_Type,Date,Address",
        [(data.corp_inf.TN,
          data.corp_inf.Jurisdiction,
          data.corp_inf.
          Number,
          data.corp_inf.Company_Type,
          data.corp_inf.Date,
          data.corp_inf.Address
          )])
    @allure.story('Verify the workflow for register '
                  'corporate account can be completed successfully.')
    @pytest.mark.skip('skop')
    def test_St091(self,drivers,
                   tradingName,Jurisdiction,Number,Company_Type,Date,Address):
        login=customer_login_page(drivers)

        with allure.step('login'):
            login.get(data.Env.url_cur_qa)



            login.email.send_keys(data.corp_inf.corp_email+data.Email_type.snapmail)
            login.password.send_keys(data.corp_inf.password);sleep(3)
            login.login_button.click()
            sleep(3)

        with allure.step('close closeProfile_SetUp'):
            page=CustomerHomePage(drivers)
           # page.closeProfile_SetUp() #关闭弹窗

        with allure.step('You can complete your corporate identity action successfully'):

             assert page.complete_your_Corporate_Identity(Jurisdiction,Number,
                                          Company_Type,Date,Address) == tradingName

        with allure.step('Complete upload company photo action at '
                         'first,it can be completed successfully'):
            page.upload_company_logo(os.getcwd() + data.corp_inf.logo)


        with allure.step('You can click your profile photo(homepage/profile page)to'
                         ' change it successfully and the upload company photo'):
            page.homepage_System()# pending
            system=Profile_Page(drivers)
            system.upload_logo(os.getcwd() + data.Photo_C.BRD)

# ------------------------------------------------------------------------------------------------#

    @pytest.mark.skip('skop')
    @allure.story('Verify that the portal should be able to search and connect with a new corporate user.')
    @allure.title('From the portal you should be able to search and connect with a new corporate')
    @pytest.mark.parametrize("InviteEmail,Password,porduct_name,Username",
                             [(data.ST_account.T94_corp_Email,
                               data.ST_account.T94_corp_Password,
                               data.ST_account.T94_corp_porduct_name,
                               data.ST_account.T94_corp_Username,
                               )])
    def test_St094_corporate(self, drivers, InviteEmail, Password, porduct_name, Username):


        mail_type=1 #选择需要查看的邮件类型
        RootPath=PathOperation()
        doc_photo=RootPath.getOtherPath('\Data')+data.Photo_C.BRD

        bus = LoginPage(drivers)
        with allure.step('Precondition: LOGIN_BUSINESS_PORTAL...'):
            bus.get(data.Env.url_devqa);sleep(3)
            bus.login_username.send_keys('kiki@snapmail.cc')
            bus.login_password.send_keys(Password)
            bus.login_button.click()


        with allure.step('A: You will need to select the product/service you are connecting for'):
            nav=NavigationBar(drivers)

            with allure.step('send invite'):
                nav.SourceDocuments(InviteEmail,porduct_name,'invite-email')

        with allure.step('B: Check mailbox'):
            '''snapmail 新增email '''
            mailbox=MailBox(drivers) # 调用脚本
            mailbox.open_Mail()
            mailbox.create_new_email(Username)

            with allure.step('Receive an email to set up a valid8me account.'):
                ''',打开发送的邮件链接'''
                invited_user_email=mailbox.email_type_call(InviteEmail, mail_type);

            with allure.step('The user use email link to customer portal'):
                #验证被邀请的邮件与跳转之后的邮件是否一致
                assert invited_user_email==InviteEmail,print("验证被邀请的邮件与跳转之后的邮件一致")

        with allure.step('C: Customer could register successfully.'):
            cus=customer_login_page(drivers)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.register_confirm_button.click();
            sleep(3)
            cus.code_input.send_keys("666666")
            cus.confirm_btu.click()
            cus.legalName.send_keys(Username)
            cus.tradingName.send_keys(Username)
            cus.register_profile_corporate_confirm_button.click();
            cus.wait_page_load_timeout(5)
            with allure.step('close closeProfile_SetUp'):
                page = CustomerHomePage(drivers)
                page.closeProfile_SetUp()  # 关闭弹窗;
                sleep(3)

        with allure.step('D: This user will check this action in my action list'):
            action = ActionPage(drivers)
            action.open_Action_Page()
            action.open_Purpose(porduct_name)

        with allure.step('E: The user uplod all need docs and click consent,'):
            action.upload_action_doc(doc_photo,Username)
            action.consent_action()
            action.open_Home_Page()

            with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                RecentShares(drivers).view_all.click();
                sleep(3)
            with allure.step('see who can access them and what documents in companies page'):
                cuss=Companies(drivers)
                cuss.ReturnSharedDocuments()

# --------------------------------------------------------------------------------------------------------------#

    @pytest.mark.skip('skop')
    @allure.story('Verify that the portal should be able to search and connect with a new corporate user.')
    @allure.title('From the portal you should be able to search and connect with a new corporate')
    @pytest.mark.parametrize("InviteEmail, Password, porduct_name, Username",
                             [(data.ST_account.T94_ind_Email,
                               data.ST_account.T94_ind_Password,
                               data.ST_account.T94_ind_porduct_name,
                               data.ST_account.T94_ind_Username,
                               )])
    def test_St094_individual(self, drivers, InviteEmail, Password, porduct_name, Username):
        mail_type = 1  # 选择需要查看的邮件类型
        '准备工作-放置文件路径'
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')

        bus = LoginPage(drivers)
        with allure.step('Precondition: LOGIN_BUSINESS_PORTAL...'):
            bus.get(data.Env.url_devqa);
            sleep(3)
            bus.login_username.send_keys('kiki@snapmail.cc')
            bus.login_password.send_keys(Password)
            bus.login_button.click()

        with allure.step('A: You will need to select the product/service you are connecting for'):
            nav = NavigationBar(drivers)

            with allure.step('send invite'):
                nav.SourceDocuments(InviteEmail, porduct_name, 'invite-email')

        with allure.step('B: Check mailbox'):
            '''snapmail 新增email '''
            mailbox = MailBox(drivers)  # 调用脚本
            mailbox.open_Mail()
            mailbox.create_new_email(Username)

            with allure.step('Receive an email to set up a valid8me account.'):
                ''',打开发送的邮件链接'''
                invited_user_email = mailbox.email_type_call(InviteEmail, mail_type);

            with allure.step('The user use email link to customer portal'):
                # 验证被邀请的邮件与跳转之后的邮件是否一致
                assert invited_user_email == InviteEmail, print("验证被邀请的邮件与跳转之后的邮件一致")

        with allure.step('C: Customer could register successfully.'):
            cus = customer_login_page(drivers)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.register_confirm_button.click();
            sleep(3)
            cus.code_input.send_keys("666666")
            cus.confirm_btu.click()
            cus.firstName.send_keys(Username)
            cus.lastName.send_keys(Username)
            cus.register_profile_individual_confirm_button.click();
            cus.wait_page_load_timeout(5)
            with allure.step('close closeProfile_SetUp'):
                page = CustomerHomePage(drivers)
                page.closeProfile_SetUp()  # 关闭弹窗;
                sleep(3)

        with allure.step('D: This user will check this action in my action list'):
            action = ActionPage(drivers)
            action.open_Action_Page()
            action.open_Purpose(porduct_name)
        dataTest = dict(data.Photo_C)
        with allure.step('E: The user uplod all need docs and click consent,'):
            action.upload_action_doc(DocPath, dataTest,Username)
            action.consent_action()
            action.open_Home_Page()

            with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                RecentShares(drivers).view_all.click();
                sleep(3)
            with allure.step('see who can access them and what documents in companies page'):
                cuss = Companies(drivers)
                cuss.ReturnSharedDocuments()

# with allure.step("Login"):
        #     cus = customer_login_page(drivers)
        #     cus.open(data.Env.dev_customer);
        #     cus.Email_Input.send_keys(email)
        #     cus.Password.send_keys(Password)
        #     cus.Login.click()
        #     cus.sleep(5)
    #@pytest.mark.skip('skop')
# ---------------------------------------------------------------------------------------------------------------#

    @allure.story('Verify that the portal should be able to search and connect with an existing corporate user..')
    @pytest.mark.skip('skop')
    @allure.title('From the portal you should be able to search and connect with a corporate customer')
    @pytest.mark.parametrize(
        "InviteEmail, Password, porduct_name, Username,business_email,business_password,business_name",
        [(Test_data['T95_corp_Email'],
          Test_data['T95_corp_Password'],
          Test_data['T95_corp_porduct_name'],
          Test_data['T95_corp_Username'],
          Test_data['business_email'],
          Test_data['business_password'],
          Test_data['business_name']

          )])
    def test_St095_96_corporate(self, drivers, InviteEmail, Password, porduct_name, Username, business_email,
                                      business_password, business_name):
        mail_type = 1  # 选择需要查看的邮件类型
        '准备工作-放置文件路径'
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')

        bus = LoginPage(drivers)
        with allure.step('Precondition: 1. Sign up a new Corp User...'):
            cus = customer_login_page(drivers)
            cus.open(Test_data['customer_url']);
            cus.sign_up.click()
            cus.register_email_field.send_keys(InviteEmail)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpCorp(Username)

            chp=CustomerHomePage(drivers)
            chp.closeProfile_SetUp()
            sleep(3)
            # '''Logout'''
            chp.Logout()
            #cus.Login_step(InviteEmail,Password)  #Test
            sleep(3)

        with allure.step('Precondition: 2. Login in Business Poratl...'):

            OpenNew_window = 'window.open("{}")'.format(Test_data['business_url'])
            bus.execute_script(OpenNew_window);
            bus.switch_to_window(1)
            bus.wait(10);
            sleep(5)
            bus.refrash()
            bus.login_username.send_keys(business_email)
            bus.login_password.send_keys(business_password)
            bus.login_button.click()
            sleep(3)
        with allure.step('A: You will need to select the product/service you are connecting for'):
            A1 = Product(drivers)
            A1.OpenProuductPage()
            A1.CreateOnlyCorp(porduct_name, Note='Autotest create')
            sleep(3)
        with allure.step('send invite'):
            A2 = NavigationBar(drivers)
            A2.OpenMyWork();
            sleep(3)

        with allure.step('B: The User on the customer portal should receive an action to consent or reject'):
        #     '''Reject action '''
            with allure.step('B1: If the user reject ,the action will disappears'):
                with allure.step('Open customer portal'):


                    cus.switch_to_window(0)
                    cus.Login_step(InviteEmail,Password)
                with allure.step('Reject ,the action'):
                    B1=ActionPage(drivers)
                    B1.open_Action_Page()
                    B1.open_Purpose(porduct_name)
                    B1.reject_action()
                #assert a in b ：判断b包含a
                with allure.step('ASSERT： action will disappears'):
                    assert "No find" in B1.open_Purpose(porduct_name)
                    CustomerHomePage(drivers).Logout()


            with allure.step('B2  : If the usercon consent, you should be able to see who can '
                             'access them and what documents they can see by clicking  ‘Recent Shares’ and ’companies’page"'
                             'Customer web'):

                B2=NavigationBar(drivers)
                B2.switch_to_window(1)
                B2.SourceDocuments(InviteEmail,porduct_name,Note='Autotest_again_invited')

                with allure.step('consent action'):
                    B2.switch_to_window(0)
                    cus.Login_step(InviteEmail, Password)
                    B3 = ActionPage(drivers)
                    B3.open_Action_Page()
                    B3.open_Purpose(porduct_name)
                    '导入数据'
                    dataTest = dict(data.Photo_C)
                    B3.upload_action_doc(DocPath, dataTest,Username)
                    # 从这里开始写】
                    B3.consent_action()
                    B3.open_Home_Page()


                #
                    with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                        RecentShares(drivers).view_all.click();
                        sleep(3)
                    with allure.step('see who can access them and what documents in companies page'):
                        B4 = Companies(drivers)
                        share=B4.ReturnSharedDocuments()
                        assert len(share['shareDocument'])>=0

            with allure.step('ST96-96A: Verify that the corporate user should be able to search for companies successfully'):
                with allure.step(' a. You will need to select a Product/Service you are connecting for and share you doc with them'):
                    B4.SearchConnect(business_name,porduct_name)
                    share = B4.ReturnSharedDocuments()
                    assert share['Recent_Product']==porduct_name

                with allure.step(' b. Login portal, the status of connection case is Granted.'):
                    B4.switch_to_window(1)
                    sleep(3)
                    B5 = NavigationBar(drivers)
                    notie = B5.CheckNotifications()
                    assert notie['Status']=='Granted';

    'st——95--individual'

# ---------------------------------------------------------------------------------------------------------#


    @allure.story('Verify that the portal should be able to search and connect with an existing individual user..')
    @allure.title('From the portal you should be able to search and connect with a individual customer')
    @pytest.mark.parametrize("InviteEmail, Password, porduct_name, Username,business_email,business_password,business_name",
                             [(Test_data['T95_ind_Email'],
                               Test_data['T95_ind_Password'],
                               Test_data['T95_ind_porduct_name'],
                               Test_data['T95_ind_Username'],
                               Test_data['business_email'],
                               Test_data['business_password'],
                               Test_data['business_name'],
                               )])
    @pytest.mark.skip('skop')
    def test_St095_96_individual(self, drivers, InviteEmail, Password, porduct_name, Username,business_email,business_password,business_name):

        '准备工作-放置文件路径'
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')

        '准备工作-创建个人用户'
        cus = customer_login_page(drivers)
        with allure.step('Precondition: 1. Sign up a new Individual User...'):

            cus.open(Test_data['customer_url']);
            cus.sign_up.click()
            cus.register_email_field.send_keys(InviteEmail)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpInd(Username)

            chp=CustomerHomePage(drivers)
            chp.closeProfile_SetUp();sleep(3)

            chp.Logout();sleep(3)
            #cus.Login_step(InviteEmail,Password)  #Test

        bus = LoginPage(drivers)
        with allure.step('Precondition: 2. Login in Business Poratl...'):

            OpenNew_window = 'window.open("{}")'.format(Test_data['business_url'])
            bus.execute_script(OpenNew_window);
            bus.switch_to_window(1)
            bus.wait(10);
            sleep(7)
            #bus.refrash()

            bus.login_username.send_keys(business_email)
            bus.login_password.send_keys(business_password)
            bus.login_button.click();sleep(3)

        with allure.step('A: You will need to select the product/service you are connecting for'):
            A1=Product(drivers)
            A1.OpenProuductPage()
            A1.CreateOnlyIndividual(porduct_name,Note='Autotest create')
            sleep(3)
            with allure.step('send invite'):
                A2=NavigationBar(drivers)
                A2.OpenMyWork();sleep(3)
                A2.SourceDocuments(InviteEmail, porduct_name, Note='invite-email')

        with allure.step('B: The User on the customer portal should receive an action to consent or reject'):
            '''Reject action '''
            with allure.step('B1: If the user reject ,the action will disappears'):
                with allure.step('Open customer portal'):

                    cus.switch_to_window(0)
                    cus.Login_step(InviteEmail,Password)
                with allure.step('Reject ,the action'):
                    B1=ActionPage(drivers)
                    B1.open_Action_Page()
                    B1.open_Purpose(porduct_name)
                    B1.reject_action()
                                                                               # assert a in b #：判断b包含a
                with allure.step('ASSERT： action will disappears'):
                    assert "No find" in B1.open_Purpose(porduct_name)
                    CustomerHomePage(drivers).Logout()

            with allure.step('B2  : If the usercon consent, you should be able to see who can access them and what documents they can see by clicking  ‘Recent Shares’ and ’companies’page"   	Customer web'):

                B1.switch_to_window(1)
                B2=NavigationBar(drivers)
                B2.SourceDocuments(InviteEmail,porduct_name,Note='Autotest_again_invited')

                with allure.step('Consent action'):
                    cus.switch_to_window(0)
                    cus.Login_step(InviteEmail, Password)
                    B3 = ActionPage(drivers)
                    B3.open_Action_Page()
                    B3.open_Purpose(porduct_name)
                    with allure.step('Upload doc which in action list'):
                        dataTest=dict(data.Photo_C)
                        B3.upload_action_doc(DocPath,dataTest,Username)

                    B3.consent_action()
                    B3.open_Home_Page()

                    with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                        RecentShares(drivers).view_all.click();
                        sleep(3)
                    with allure.step('see who can access them and what documents in companies page'):
                        B4 = Companies(drivers)
                        share = B4.ReturnSharedDocuments()
                        assert len(share['shareDocument']) >= 0

        with allure.step(
                'ST96-96A: Verify that the individual user should be able to search for companies successfully'):
            with allure.step(
                    ' a. You will need to select a Product/Service you are connecting for and share you doc with them'):
                B4.SearchConnect(business_name, porduct_name)
                share = B4.ReturnSharedDocuments()
                assert share['Recent_Product'] == porduct_name

            with allure.step(' b. Login portal, the status of connection case is Granted.'):
                B4.switch_to_window(1)
                sleep(3)
                B5 = NavigationBar(drivers)
                notie = B5.CheckNotifications()
                assert notie['Status'] == 'Granted';
# ----------------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------------------------#
    @allure.story('Verify that the corporate user should be able to upload a document..')
    @pytest.mark.skip('skop')
    @pytest.mark.parametrize(
        "InviteEmail, Password, Username,UploadDocName",
        [(Test_data['T97_corp_Email'],
          Test_data['T97_corp_Password'],
          Test_data['T97_corp_Username'],
          Test_data['T97_corp_UploadDocName'],
          )])
    def test_St097_98_corporate(self, drivers, InviteEmail, Password, Username, UploadDocName):
        '准备工作-放置文件路径'
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')
            dataTest = dict(data.Photo_C)# 加载 文档内容

        CustomerHomePage_= CustomerHomePage(drivers)
        with allure.step('Precondition: 1. Sign up a new Corp User...'):
            cus = customer_login_page(drivers)
            cus.open(Test_data['customer_url']);
            cus.sign_up.click()
            cus.register_email_field.send_keys(InviteEmail)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpCorp(Username)
            CustomerHomePage_.closeProfile_SetUp()
            sleep(3)
            #cus.Login_step(InviteEmail,Password)  #Test

        DocumentPage = Document(drivers)
        with allure.step('St97: On the customer web you should be able to upload a document.'):

            with allure.step('A: Upload doc in Home page'):
                CustomerHomePage_.UploadDocHome_Corp(DocPath, dataTest, UploadDocName)
            with allure.step('B: Upload doc in document page'):

                UploadResult = DocumentPage.UploadDocDocumentPage_Corp(DocPath, dataTest, UploadDocName)
                assert UploadResult == True

        with allure.step('St98: Verify that corporate user should be able to Update/Delete document'):
            with allure.step('A1:You should be able update document by click update button next to one document'):

                assert DocumentPage.UpdateDocDocumentPage_Corp(DocPath, dataTest, UploadDocName)

            with allure.step('A2:You should be able update document by click update button next to one document'):
                assert DocumentPage.DeleteDocDocumentPage_Corp(DocPath, dataTest, UploadDocName)


#--------------------------------------------------------------------------------------------------------------------------#
    @allure.story('Verify that the corporate user should be able to upload a document..')
    @pytest.mark.skip('skop')
    @pytest.mark.parametrize(
        "InviteEmail, Password, Username,UploadDocName",
        [(Test_data['T97_ind_Email'],
          Test_data['T97_ind_Password'],
          Test_data['T97_ind_Username'],
          Test_data['T97_ind_UploadDocName'],
          )])
    def test_St097_98_individual(self, drivers, InviteEmail, Password, Username, UploadDocName):
        '准备工作-放置文件路径'
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')
            dataTest = dict(data.Photo_C)# 加载 文档内容

        CustomerHomePage_= CustomerHomePage(drivers)
        with allure.step('Precondition: 1. Sign up a new Individual User...'):
            cus = customer_login_page(drivers)
            cus.open(Test_data['customer_url']);
            cus.sign_up.click()
            cus.register_email_field.send_keys(InviteEmail)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpInd(Username)
            CustomerHomePage_.closeProfile_SetUp()
            sleep(3)
            # cus.Login_step(InviteEmail,Password)  #Test
            cus.wait_page_load_timeout(10)

        DocumentPage = Document(drivers)
        with allure.step('St97: On the customer web you should be able to upload a document.'):

            with allure.step('A: Upload doc in Home page'):
                CustomerHomePage_.UploadDocHome_Ind(DocPath, dataTest, UploadDocName,Username)
            with allure.step('B: Upload doc in document page'):

                UploadResult = DocumentPage.UploadDocDocumentPage_ind(DocPath, dataTest, UploadDocName)
                assert UploadResult == True

        with allure.step('St98: Verify that individual user should be able to Update/Delete document'):
            with allure.step('A1:You should be able update document by click update button next to one document'):

                assert DocumentPage.UpdateDocDocumentPage_Ind(DocPath, dataTest, UploadDocName)

            with allure.step('A2:You should be able update document by click update button next to one document'):
                assert DocumentPage.DeleteDocDocumentPage_IND(DocPath, dataTest, UploadDocName)


#--------------------------------------------------------------------------------------------------------------------------#
    @allure.story('Verify that the corporate user should be able to upload a document..')
    #@pytest.mark.skip('skop')
    @pytest.mark.parametrize(
        "CorpEmail,CorpName,"
        "Rep1Email,Rep1Name,"
        "Rep2Email,Rep2Name,DocumentType1,Rep2Doc2,"
        "Rep3Email,Rep3Name,DocumentType2,Password,"
        "business_name,NewProductName,business_email,business_password",
        [(Test_data['T110_CorpEmail'],Test_data['T110_CorpName'],

          Test_data['T110_Rep1Email'],Test_data['T110_Rep1Name'],

          Test_data['T110_Rep2Email'], Test_data['T110_Rep2Name'], Test_data['T110_DocumentType1'], Test_data['T110_Rep2Doc2'],

          Test_data['T110_Rep3Email'], Test_data['T110_Rep3Name'], Test_data['T110_DocumentType2'],

          Test_data['T110_Password'],

          Test_data['business_name'], Test_data['T110_NewProductName'], Test_data['business_email'], Test_data['business_password'],
          )])
    def test_St110(self, drivers, CorpEmail, CorpName,
                   Rep1Email, Rep1Name,
                   Rep2Email, Rep2Name,DocumentType1, Rep2Doc2,
                   Rep3Email, Rep3Name, DocumentType2,
                   Password,
                   business_name, NewProductName,business_email, business_password):
        RootPath = PathOperation()
        with allure.step('Precondition 0: Doc Type Path Ready....'):
            DocPath = RootPath.getOtherPath('\Data')
            dataTest = dict(data.Photo_C)  # 加载 文档内容

        CusHomePage=CustomerHomePage(drivers)
        cus = customer_login_page(drivers)
        cus.open(Test_data['customer_url']);
        with allure.step('Precondition 1: Sign up a individual user:{}'.format(Rep1Email)):
            cus.sign_up.click()
            cus.register_email_field.send_keys(Rep1Email)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpInd(Rep1Name)
            sleep(3)
            CusHomePage.closeProfile_SetUp()
            # cus.Login_step(InviteEmail,Password)  #Test
            cus.wait_page_load_timeout(10)
            CusHomePage.Logout()
        with allure.step('Precondition 2: Sign up a Corporate user:{}'.format(CorpEmail)):
            cus.sign_up.click()
            cus.register_email_field.send_keys(CorpEmail)
            cus.register_password_field.send_keys(Password)
            cus.register_passwordRepeat_field.send_keys(Password)
            cus.accept_read.click()
            cus.SignUpCorp(CorpName)
            CusHomePage.closeProfile_SetUp()
            # cus.Login_step(CorpEmail,Password)  # Test

        ActionOP = ActionPage(drivers)
        corpRep = CorpRep(drivers)
        AuthPage = AuthRep(drivers)
        with allure.step('A. Verify the workflow of corporate send invite 1 existing user:{}and 2 new users:{},{} as the auth reps at the time.'.format(Rep1Email,Rep2Email,Rep3Email)):
            with allure.step('1. Click Add Authorised Representatives to add online 3 reps'):
                ActionOP.AddOnlineRep(Rep1Email,Rep2Email,Rep3Email)
                CusHomePage.Logout()
        with allure.step('B. Verify the workflow of individual user become an anthorized representative.'):
            with allure.step('Scenario 1: The individual user {} has not uploaded any documents.'.format(Rep1Email)):
                cus.Login_step(Rep1Email,Password)

                with allure.step('Confirm anthorized representative action'):
                    ActionOP.ConfirmAuteRep_With_No_Doc()

                with allure.step('Corporates I represent has this corporate name:{}'.format(CorpName)):
                    obtained_Information=corpRep.CheckCorpInformation()
                    assert obtained_Information['getcorpName']==CorpName
                    assert len(obtained_Information['getDocWithAccess'])==0 #判断是否为空字符串
                with allure.step('Logout this user'):
                    CusHomePage.Logout()

            with allure.step('Scenario 2: The individual user {} has uploaded some documents that with only one version.'.format(Rep2Email)):
                with allure.step('The individual user sign up successfuly'):
                    cus.FirstSignInd(Rep2Email,Password,Rep2Name)
                    CusHomePage.closeProfile_SetUp()
                    cus.Login_step(Rep2Email,Password) #  test

                with allure.step('Upload one document'):
                    CusHomePage.UploadDocHome_Ind(DocPath, dataTest, DocumentType1,Rep2Name)

                with allure.step('Confirm anthorized representative action, and shared doc {} to corporate'.format(DocumentType1)):
                    ActionOP.ConfirmAuteRep_WithDocs(DocumentType1)

                with allure.step('Corporates I represent has this corporate name:{} with shared doc {}'.format(CorpName,DocumentType1)):
                    obtained_Information=corpRep.CheckCorpInformation()
                    assert obtained_Information['getcorpName']==CorpName
                    assert DocumentType1 in obtained_Information['getDocWithAccess']

                with allure.step('Logout this user'):
                    CusHomePage.Logout()

            with allure.step('Scenario 3 :The user {} has uploaded some documents that with multiple versions.'.format(Rep3Email)):
                with allure.step('The individual user sign up successfuly'):
                    cus.FirstSignInd(Rep3Email, Password, Rep3Name)
                    CusHomePage.closeProfile_SetUp()
                    #cus.Login_step(Rep3Email,Password) #Test

                with allure.step('Upload multiple docs versions. Version ==2'):
                    CusHomePage.UploadDocHome_Ind(DocPath, dataTest, DocumentType2,Rep2Name)
                    CusHomePage.UploadDocHome_Ind(DocPath, dataTest, DocumentType2,Rep2Name)
                    assert CusHomePage.GetDoclatestVersion(DocumentType2)=='Version 2'

                with allure.step('Confirm anthorized representative action, and shared doc {} to corporate'.format(DocumentType2)):
                    ActionOP.ConfirmAuteRep_WithDocs(DocumentType2)

                with allure.step('Corporates I represent has this corporate name:{} with shared doc {}'.format(CorpName,DocumentType2)):
                    obtained_Information=corpRep.CheckCorpInformation()
                    assert obtained_Information['getcorpName']==CorpName
                    assert DocumentType2 in obtained_Information['getDocWithAccess']

                with allure.step('Logout this user'):
                    CusHomePage.Logout()
        #
        #

            document = Documents_Corp(drivers)
            with allure.step('Assert The rep display results'):
                with allure.step('Login corporate'):
                    cus.Login_step(CorpEmail,Password)

                with allure.step('Check Connections/Authorised Representatives page'):
                    with allure.step('CHeck rep name and shared doc Coincident'):
                        getAuthInfor = AuthPage.CheckAuthInformation()
                        assert len(getAuthInfor[Rep1Email])==0
                        assert DocumentType1 in getAuthInfor[Rep2Email]
                        assert DocumentType2 in getAuthInfor[Rep3Email]

                    document.open_Documents()
                    document.open_Representatives()
                    with allure.step('{} has no doc '.format(Rep1Name)):
                        document.open_OnlineRepPage(Rep1Name)
                        assert document.NOdoc_isExist()==True
                    with allure.step('{} has one doc {} latest doc is 1'.format(Rep2Name,DocumentType1)):

                        document.open_OnlineRepPage(Rep2Name)
                        assert document.check_repDocDetails(DocumentType1)=='Version 1'
                        document.close_doc_window()

                    with allure.step('{} has one doc {} latest doc version is 2'.format(Rep3Name,DocumentType2)):

                        document.open_OnlineRepPage(Rep3Name)
                        assert document.check_repDocDetails(DocumentType2) == 'Version 2';
                        #document.close_doc_window()
                    with allure.step('For {} Previous versions of this document will show NO ACCESS in details and cannot request to view'.format(Rep3Name)):

                        document.latestV.click()
                        document.PreviousV.click();sleep(3)
                        assert document.docIs_NoAccess()==True
                        document.close_doc_window()
                        CusHomePage.Logout()
        with allure.step('C: Verify the workflow of the existing rep {} upload new version of the document that has granted access for the corporate company.'.format(Rep2Email)):
            with allure.step('Login rep account and Upload new version of document{}'.format(DocumentType1)):
                cus.Login_step(Rep2Email,Password)
                CusHomePage.UploadDocHome_Ind(DocPath,dataTest,DocumentType1)
                with allure.step('Rep Logout'):
                    CusHomePage.Logout()

            document = Documents_Corp(drivers)
            with allure.step('Login the corporate account.'):

                cus.Login_step(CorpEmail, Password)
            with allure.step('Switch to This rep Documents tab page.'):

                document.open_Documents()
                document.open_Representatives()
                document.open_OnlineRepPage(Rep2Name)
            with allure.step(' There is "NEW" at the top-left corner of the document {} '.format(DocumentType1)):
                assert document.check_NewLabel(DocumentType1)
            with allure.step('Check Document and has a "Request Access" button at the document.'):
                latestVersion = document.check_repDocDetails(DocumentType1)
                document.requestAccessButton.click()
            with allure.step('Input Note and confirm'):
                document.note.send_keys('The {} Access Request'.format(latestVersion))
                document.confirmNote.click();time.sleep(3)
            with allure.step('The new version will be displayed.'):
                assert document.docIs_NoAccess()==False
                document.close_doc_window()
                CusHomePage.Logout()
            massageP=MessagesPage(drivers)
            with allure.step('Login rep account ,in notification named "Important Info" will be displayed.'):
                cus.Login_step(Rep2Name,Password)
                massageP.JumpSytemMessage()
                assert 'The {} Access Request'.format(latestVersion) in massageP.GetLatestMassage()
                CusHomePage.Logout()
        document = Documents_Corp(drivers)

        with allure.step('D: Verify the workflow of the corporate request access to rep {} one document that he without the access before'.format(Rep2Email)):
            with allure.step('Rep upload a new type doc name {}'.format(Rep2Doc2)):
                cus.Login_step(Rep2Email,Password)
                CusHomePage.UploadDocHome_Ind(DocPath,dataTest,Rep2Doc2)
                CusHomePage.Logout()


            with allure.step('Switch to This rep Documents tab page.'):

                cus.Login_step(CorpEmail,Password)
                document.open_Documents()
                document.open_Representatives()
                document.open_OnlineRepPage(Rep2Name)
            with allure.step('There is "No Access" at the top-left corner of the document {} '.format(Rep2Doc2)):

                assert document.check_NoAccess_Label(Rep2Doc2)
            with allure.step('Send Document Permission Request '):

                document.note.send_keys('The {} Access Request'.format(Rep2Doc2))
                document.confirmNote.click();time.sleep(3)
                CusHomePage.Logout()

            with allure.step('Rep login and Document Permission Request display in the action list'):
                cus.Login_step(Rep2Email,document)
                #后面会修复 为
                ActionOP.open_Purpose('requested access to the below document(s)')
                ActionOP.Confirm_DocPermission()
                with allure.step('Check Corporates I represent displays doc {}'.format(Rep2Doc2)):

                    AccessDoc = CorpRep.CheckCorpInformation()
                    assert Rep2Doc2 in AccessDoc['getDocWithAccess']
                    CusHomePage.Logout()
            with allure.step('Coporate login can see the details of the doc {}'.format(Rep2Doc2)):
                cus.Login_step(CorpRep,Password)
                document.open_Documents()
                document.open_Representatives()
                document.open_OnlineRepPage(Rep2Name)
                assert document.check_repDocDetails(Rep2Doc2)
                CusHomePage.Logout()

        product_op = Product(drivers)
        bus = LoginPage(drivers)
        nav = NavigationBar(drivers)
        corpRep = CorpRep(drivers)

        with allure.step('Precondition 1: {} create a new product name {}...'.format(business_name, NewProductName)):
            with allure.step('Login business portal...'):
                OpenNew_window = 'window.open("{}")'.format(Test_data['business_url'])
                bus.execute_script(OpenNew_window);
                bus.switch_to_window(1)
                bus.wait(10);
                sleep(7)
                # bus.refrash()
                bus.BusLogin(business_email, business_password)
            with allure.step('Create a new Product/Services named {}'.format(NewProductName)):
                product_op.OpenProuductPage()
                product_op.Create_Basic_Inforamtion(NewProductName, 'Corporate',
                                                    Note='Scenario 1: The corporate company has shared the document to OBC')
                product_op.Create_Standard_Due_Diligence_Documents()
                product_op.Create_Authorised_Representatives(1, DocumentType1)
            with allure.step('Send to {} Source documents'.format(CorpEmail)):
                nav.SourceDocuments(CorpEmail, NewProductName,
                                    Note='Scenario 1: The corporate company has shared the document to OBC')
                nav.switch_to_window(0)
            with allure.step('Corp completed this new product'):
                cus.Login_step(CorpEmail,Password)
                ActionOP.open_Purpose(NewProductName)
                ActionOP.rep_name.is_exist()
                ActionOP.Next.click();
                ActionOP.Select_rep(Rep2Name)
                ActionOP.consent_action()
                CusHomePage.Logout()

        with allure.step('E: Verify the workflow of the existing rep revoke the document that has granted access for the corporate company.'):
            with allure.step('Scenario 1: The corporate company has shared the document to OBC: {}'.format(business_name)):

                with allure.step('Rep login and revoke this doc {}'.format(Rep2Doc2)):
                    cus.Login_step(Rep2Email, Password)
                    corpRep.open_CorporatesRepresent()
                    with allure.step('The document has been shared with onboarding company, please revoke access first.'):
                        assert corpRep.reovkeDoc(Rep2Doc2) ==False

            with allure.step('Scenario 2: The corporate company has not shared the document to any OBC: {}'.format(business_name)):

                with allure.step('Rep login and revoke this doc {}'.format(DocumentType1)):

                    with allure.step( 'Revoke button will be disappeared next the document.'):
                        assert corpRep.reovkeDoc(DocumentType1) == True
                    with allure.step(' Login the corporate account ->Switch to Documents tab page.'):
                        cus.Login_step(CorpEmail, Password)
                    with allure.step('There is "No Access" at the document {} '.format(DocumentType1)):

                        document.open_Documents()
                        document.open_Representatives()
                        with allure.step('{} has no doc '.format(DocumentType1)):
                            document.open_OnlineRepPage(Rep1Name)
                            assert document.check_NoAccess_Label(DocumentType1,click=False)==True
                            CusHomePage.Logout()

        with allure.step('F: Verify the workflow of the existing rep delete the document that has granted access for the corporate company'):
            with allure.step('Scenario 1: The corporate company has shared the document{} to OBC.'.format(Rep2Doc2)):
                with allure.step('1. Login the rep account'):
                    cus.Login_step(Rep2Email,Password)
                with allure.step('2. Switch to Documents tab page.'):
                    document.open_Documents()
                with allure.step('3. Delete the document that has been shared to OBC.'):
                    daleteResult = document.Delete_Doc(Rep2Doc2)
                with allure.step('One info pop up will be displayed: The document has been shared with onboarding company, please revoke access first.'):
                    assert daleteResult[0]==False
                    assert daleteResult[1] in 'The document has been shared with onboarding company,'

            with allure.step('Scenario 2: The corporate company has no shared the document{} to OBC.'.format(DocumentType1)):

                with allure.step('1 Delete the document {} that not shared to OBC.'.format(DocumentType1)):
                    daleteResult = document.Delete_Doc(DocumentType1)
                with allure.step(' The document will be disappeared in My Document page.'):
                    assert daleteResult[0]==True
            CusHomePage.Logout()

        with allure.step('G:  Verify the workflow of the corporate company remove the existing rep and invite he as the rep again.'):
            with allure.step('Scenario 1: The corporate company has shared the rep document to OBC.'):
                with allure.step('1. Login the corp account'):
                    cus.Login_step(CorpEmail, Password)
                with allure.step('2. Navigate to connections/Authorised Representative'):
                    AuthPage.open_AuthorisedRepresent()
                with allure.step('3. Choose a Rep and click the delete button Click the CONFIRM button  Refresh the list'):
                    assert AuthPage.Remove_onlineRep(Rep2Email)==True
                with allure.step('4. Check the in Document-Inactive'):

                    document.open_Documents()
                    document.open_InactiveRepPage(Rep2Email)
                    CusHomePage.Logout()
                with allure.step('5.Rep login and Switch to connections-Corporates Represent'):

                    cus.Login_step(Rep2Email,Password)
                    corpRep.open_CorporatesRepresent()
                with allure.step('6 The documents which has be shared to OBC are displayed in the documents permission page.'):

                    corpRep.PermissionSetting.click()
                with allure.step('7 Pop up warning:You are no longger the representative of the Corporates I represent and cannot modify the document permission'):

                    assert 'You are no longger the representative of' in corpRep.warning.text
                    corpRep.okay.click()
                    CusHomePage.Logout()
                with allure.step('8.Login the corp account and Invite the individual as the rep again.'):

                    cus.Login_step(CorpEmail, Password)
                    AuthRep.open_AuthorisedRepresent()
                    AuthRep.InviteRep(Rep2Email)
                    CusHomePage.Logout()
                with allure.step('9.Rep Login and accept this invite'):

                    cus.Login_step(Rep2Email, Password)
                    ActionOP.open_Purpose('Confirmation needed as an Authorised representative')
                    ActionOP.confirmBeRepFirstConsent.click()
                with allure.step('10.Check if there is version information for previously shared files:This version of document {} has already been shared with this company'.format(Rep2Doc2)):

                    result = ActionOP.assertDocHasBeenShared(Rep2Doc2)
                    assert 'This version of document {} has already been shared with this company'.format(Rep2Doc2) in result[1]
                    ActionOP.docPermissionConfirm();ActionOP.sleep(3)
                    CusHomePage.Logout()
                with allure.step('11.Login corp ,Switch to the Document page.Expand the corresponding rep to check the documents.'):
                    cus.Login_step(CorpEmail,Password)
                    document.open_Documents()
                    document.open_Representatives()
                    document.open_OnlineRepPage(Rep2Name)
                with allure.step('12. The documents which selected and the documents that has shared with OBC are all with the access.'):
                    document.check_repDocDetails(Rep2Doc2)
                    assert document.close_doc_window()
                    CusHomePage.Logout()

            with allure.step('Scenario 2: The corporate company has not shared the document to any OBC.'):
                cus.Login_step(CorpEmail, Password)
                with allure.step('2. Navigate to connections/Authorised Representative'):
                    AuthPage.open_AuthorisedRepresent()
                with allure.step('3. Choose a Rep and click the delete button Click the CONFIRM button  Refresh the list'):

                    assert AuthPage.Remove_onlineRep(Rep1Email) == True
                    CusHomePage.Logout()
                with allure.step('4 Login the rep account,Switch to connections-Corporates Represent,Find the corp you just matched'):

                    cus.Login_step(Rep1Email, Password)
                    result_ = CorpRep.CheckCorpInformation()
                    assert result_['getcorpName']==''
                    CusHomePage.Logout()
                with allure.step('5.Login the corp account and Invite the individual as the rep again.'):

                    cus.Login_step(CorpEmail, Password)
                    AuthRep.open_AuthorisedRepresent()
                    AuthRep.InviteRep(Rep1Email)
                    CusHomePage.Logout()
                with allure.step('6.Rep Login and accept this invite'):

                    cus.Login_step(Rep1Email, Password)
                    ActionOP.ConfirmAuteRep_With_No_Doc()
                    CusHomePage.Logout()
                with allure.step('7.Login corp ,Switch to the Document page.Expand the corresponding rep to check the documents.'):

                    cus.Login_step(CorpEmail, Password)
                    document.open_Documents()
                    document.open_Representatives()
                    assert document.open_OnlineRepPage(Rep1Name)==True
                    CusHomePage.Logout()



























































































if __name__ == '__main__':

    # pytest.main(['-vs','../test_demo/SmokeTesting_test.py', "--alluredir=./temp_st"])
    # pytest.main(['-vs', '../test_demo/SmokeTesting_test.py'])
    pytest.main(["-vs", current_path+"\SmokeTesting_test.py"])
#
#
#     os.system("allure generate ./temp_st -o ./report_st --clean")



















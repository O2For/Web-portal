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
            action.open_new_prod_action(porduct_name)

        with allure.step('E: The user uplod all need docs and click consent,'):
            action.upload_action_doc(doc_photo)
            action.consent_action()
            action.open_Home_Page()

            with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                RecentShares(drivers).view_all.click();
                sleep(3)
            with allure.step('see who can access them and what documents in companies page'):
                cuss=Companies(drivers)
                cuss.ReturnSharedDocuments()

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
        RootPath = PathOperation()
        doc_photo = RootPath.getOtherPath('\Data') + data.Photo_C.BRD

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
            action.open_new_prod_action(porduct_name)

        with allure.step('E: The user uplod all need docs and click consent,'):
            action.upload_action_doc(doc_photo)
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

    @pytest.mark.parametrize("InviteEmail, Password, porduct_name, Username,business_email,business_password",
                             [(Test_data['T95_corp_Email'],
                               Test_data['T95_corp_Password'],
                               Test_data['T95_corp_porduct_name'],
                               Test_data['T95_corp_Username'],
                               Test_data['business_email'],
                               Test_data['business_password']

                               )])
    @allure.story('Verify that the portal should be able to search and connect with an existing corporate user..')
    @allure.title('From the portal you should be able to search and connect with a corporate customer')

    def test_St095_corporate(self, drivers, InviteEmail, Password, porduct_name, Username,business_email,business_password):
        mail_type = 1  # 选择需要查看的邮件类型
        RootPath = PathOperation()
        doc_photo = RootPath.getOtherPath('\Data') + data.Photo_C.BRD

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
            # #
            chp=CustomerHomePage(drivers)
            chp.closeProfile_SetUp()
            sleep(3)
            # '''Logout'''
            chp.Logout()
            sleep(3)
            #cus.Login_step(InviteEmail,Password)  #Test

        with allure.step('Precondition: 2. Login in Business Poratl...'):
            print(Test_data['business_email'])


            OpenNew_window = 'window.open("{}")'.format(Test_data['business_url'])
            chp.execute_script(OpenNew_window);

            chp.switch_to_window(1)
            chp.wait(10)


            bus.login_username.send_keys(business_email)
            bus.login_password.send_keys(business_password)
            bus.login_button.click()
            sleep(3)

        with allure.step('A: You will need to select the product/service you are connecting for'):
            A1=Product(drivers)
            A1.OpenProuductPage()
            A1.CreateOnlyCorp(porduct_name,Note='Autotest create')
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
                    B1.open_new_prod_action(porduct_name)
                    B1.reject_action()
                #assert a in b ：判断b包含a
                with allure.step('ASSERT： action will disappears'):
                    assert "No find" in B1.open_new_prod_action(porduct_name)
                    CustomerHomePage(drivers).Logout()


            with allure.step('B2  : If the usercon consent, you should be able to see who can access them and what documents they can see by clicking  ‘Recent Shares’ and ’companies’page"   	Customer web'):

                B1.switch_to_window(1)
                B2=NavigationBar(drivers)
                B2.SourceDocuments(InviteEmail,porduct_name,Note='Autotest_again_invited')

                with allure.step('consent action'):
                    B2.switch_to_window(0)
                    cus.Login_step(InviteEmail, Password)
                    B3 = ActionPage(drivers)
                    B3.open_Action_Page()
                    B3.open_new_prod_action(porduct_name)
                    B3.upload_action_doc(doc_photo)
                    #从这里开始写】
                    B3.consent_action()
                    B3.open_Home_Page()

                    with allure.step('see who can access them and what documents they can see by clicking ‘Recent Shares’'):
                        RecentShares(drivers).view_all.click();
                        sleep(3)
                    with allure.step('see who can access them and what documents in companies page'):
                        B4 = Companies(drivers)
                        shareDocument=B4.ReturnSharedDocuments()
                        assert len(shareDocument)>=0





























if __name__ == '__main__':

    #pytest.main(['-vs','../test_demo/SmokeTesting_test.py', "--alluredir=./temp_st"])
    #pytest.main(['-vs', '../test_demo/SmokeTesting_test.py'])
    pytest.main(["-vs", current_path+"\SmokeTesting_test.py","--alluredir=./temp_st"])


    os.system("allure generate ./temp_st -o ./report_st --clean")

#上jenkns:pytest -vs ./test_demo/SmokeTesting_test.py

# '--workers=1', '--tests-per-worker=1'
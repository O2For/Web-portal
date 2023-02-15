import os
import sys
#校验路径
sys.path.append(os.getcwd())

from selenium import webdriver
#POB
from PageObject.customer_login import *
from PageObject.snapmail_page import *
from PageObject.customer_system_page import *
from PageObject.business_login import LoginPage
from PageObject.dashborad_page import *
from PageObject.customer_connections_companies_page import *
from PageObject.customer_action_page import *
from PageObject.message_template_page import Template
#
from selenium.webdriver.common.by import By


from time import sleep
import pytest
import allure
import re
from pytest_assume.plugin import assume
# DBsql
from Common.db_server import DbMysql

from PageObject.test_page import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# 数据准备导入路径
from Common.config import YamlOperation

#----------------------------------------------
os.chdir(os.path.abspath('.') + '/Data')
# 读取yaml数据文件
data = YamlOperation(os.getcwd() + "\data.yaml")


@allure.epic('Somke Testing Valid8Me v2.8.0')
class TestCaes:
    #@allure.feature('Verify that the corporate user could be set up successfully.')
    @allure.severity("blocker")
    @pytest.mark.skip('copr 跳过')
    @pytest.mark.parametrize("terms_title,reg__corp_email,Email_type,reg_pwd,mailbox,legalName,tradingName",
                             [("End user-terms",data.corp_inf.corp_email,data.Email_type.snapmail,
                               data.corp_inf.password,data.Env.test_mail,
                               data.corp_inf.corp_email,data.corp_inf.TN)])

    @allure.story('Verify that the corporate user could be set up successfully.')
    def test_St089(self,drivers,terms_title,reg__corp_email,Email_type,
                   reg_pwd,mailbox,legalName,tradingName):
        page = customer_login_page(drivers)
        with allure.step('You should then read and accept the terms'
                         ' and conditions if you are happy with them.'):
            with allure.step('Open Valid8me customer portal'):
                page.open(data.Env.url_cur_qa)

                page.sign_up.click();sleep(2)
                with allure.step('Read and accept the terms'):
                    page.terms.click()
                    #
                    page.switch_to_window(1)
                    with assume: assert terms_title in page.terms_title.get_attribute('textContent'),'没有条款'
                    #page.accept_read.click()
        with allure.step('You will have to enter your email address '
                         'and password and confirm this password.'):
            page.switch_to_window(0)
            with allure.step('Check confirm button is_disenabled without infer'):
                with assume: assert not page.register_confirm_button.click()
            with allure.step('Input email & password & confirm password'):
                page.register_email_field.send_keys(reg__corp_email+Email_type)
                page.register_password_field.send_keys(reg_pwd)
                page.register_passwordRepeat_field.send_keys(reg_pwd)
                page.accept_read.click()
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
                             [("End user-terms",data.Email_type.snapmail,
                               data.corp_inf.password,data.Env.test_mail,
                               data.ind_inf.ind_email,data.ind_inf.FN,data.ind_inf.LN)])
    @allure.story('When setting up a individual account:')
    @pytest.mark.skip('indivdual 跳过')
    def test_St090(self,drivers,terms_title,reg_ind_email,Email_type,
                   reg_pwd,mailbox_url,FN,LN):
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
        [(data.corp_inf.TN,data.corp_inf.Jurisdiction,data.corp_inf.
          Number,data.corp_inf.Company_Type,data.corp_inf.Date,data.
          corp_inf.Address)])
    @allure.story('Verify the workflow for register '
                  'corporate account can be completed successfully.')
    @pytest.mark.skip('skop')
    def test_St091(self,drivers,tradingName,Jurisdiction,Number,Company_Type,Date,Address):
        login=customer_login_page(drivers)

        with allure.step('login'):
            login.open(data.Env.url_cur_qa)
            login.email.send_keys(data.corp_inf.corp_email+data.Email_type.snapmail)
            login.password.send_keys(data.corp_inf.password)
            login.login_button.click()
            sleep(3)

        with allure.step('close closeProfile_SetUp'):
            page=CustomerHomePage(drivers)
            page.closeProfile_SetUp() #关闭弹窗

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

    #@pytest.mark.skip('skop')
    #@allure.description('这个是描述')
    @allure.story('Verify that the portal should be able to search and connect with a new corporate user.')
    @allure.title('这个是标题')
    @allure.step('这个是步骤')

    #def test_St094(self,drivers,login_username,login_password,newemail,product):
    def test_St094(self,drivers):

        #email='to10@mfk.app';
        email = '4c1@snapmail.cc';

        password='Ht@12345'
        porduct_name='AUTO_T'
        #porduct_name = 'corp'

        username='to10'
        mail_type=1

        doc_photo=os.getcwd() + data.Photo_C.BRD
        bus = LoginPage(drivers)
        # with allure.step('login_business_portal'):
        #
        #
        #     bus.open(data.Env.url_devqa);sleep(3)
        #     bus.login_username.send_keys('gulong@snapmail.cc')
        #     bus.login_password.send_keys('Ht@12345')
        #     bus.login_button.click()
        # with allure.step('You will need to select the product/service you are connecting for'):
        #
        #     nav=NavigationBar(drivers)
        #     with allure.step('send invite'):
        #         nav.global_search_invite(email,porduct_name,'invite-email')
        #     with allure.step('Check mailbox'):
        #
        #         mailbox=MailBox(drivers) # 调用脚本
        #         mailbox.open_Mail()
        #         mailbox.create_new_email(username)
        #     with allure.step('Receive an email to set up a valid8me account.'):
        #         email_name=mailbox.email_type_call(email, mail_type);
        #     with allure.step('The user use email link to customer portal'):
        #         assert email_name==email
        #
        #     with allure.step('Customer could register successfully.'):
        #         cus=customer_login_page(drivers)
        #         cus.register_password_field.send_keys(password)
        #         cus.register_passwordRepeat_field.send_keys(password)
        #
        #         cus.accept_read.click()
        #         cus.register_confirm_button.click();
        #         sleep(3)
        #         cus.code_input.send_keys("666666")
        #         cus.confirm_btu.click()
        #         cus.legalName.send_keys(username)
        #         cus.tradingName.send_keys(username)
        #         cus.register_profile_corporate_confirm_button.click();sleep(3)
        #         with allure.step('close closeProfile_SetUp'):
        #             page = CustomerHomePage(drivers)
        #             page.closeProfile_SetUp()  # 关闭弹窗;
        #             sleep(3)

        '''此处是单独的customer portal 登录脚本'''
        cuss=customer_login_page(drivers)
        cuss.open(data.Env.newqa);sleep(3)
        cuss.email.send_keys(email)
        cuss.password.send_keys(password)
        cuss.login.click();sleep(3)
        #action=ActionPage(drivers)
        # with allure.step('d. This user will check this action in my action list'):
        #     action.open_Action_Page()
        #     action.open_new_prod_action(porduct_name)

        # with allure.step('e. The user uplod all need docs and click consent,'):
        #     action.upload_action_doc(doc_photo)
        #     action.consent_action()
        with allure.step('The user uplod all need docs and click consent,should be able to see who can access them and what documents they can see by clicking  ‘Recent Shares’ and companies page'):
            RecentShares(drivers).view_all.click();sleep(3)
            cuss=Companies(drivers)
            document_list=cuss.ReturnSharedDocuments()
            assert 1!=1




    # def test_myheng(self,drivers):
    #     ht=Ht(drivers)
    #     ht.open("https://cas.hengtiansoft.com:8443/cas/login?service=http%3a%2f%2fmyhengtian%3a8033%2f");sleep(1)
    #     ht.un.send_keys("jianghaodong")
    #     ht.pd.send_keys(data.My.pd)
    #     ht.go.click();sleep(3)
    #     #ht.tt.click();sleep(1)
    #     ht.dr.click();sleep(3)
    #     ht.des.send_keys("v8 test")
    #     ht.commit.click();sleep(3)
























# if __name__ == '__main__':
#     pytest.main(['-vs','../test_demo/SmokeTesting_test.py', "--alluredir=./temp_st"])
#     #pytest.main(['-vs', '../test_demo/SmokeTesting_test.py'])
#     os.system("allure generate ./temp_st -o ./report_st --clean")


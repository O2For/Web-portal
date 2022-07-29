import os
import sys
#校验路径
sys.path.append(os.getcwd())
print(sys.path.append(os.getcwd()))
from selenium import webdriver
#POB
from PageObject.login_page import Login_page
from PageObject.Invitation import invitation_page
from PageObject.subscript import subscript

from time import sleep
import pytest
import allure
import re
# DBsql
from Common.db_server import DbMysql


# 数据准备导入路径
from Common.config import YamlOperation

#----------------------------------------------
#上jenkins要打开
#两个点点pychram 可以用。      一个点点 jenkins可以用
os.chdir(os.path.abspath('..') + '/Data')
# 读取yaml数据文件
data = YamlOperation(os.getcwd() + "\data.yaml")

#------------------------------------------------
#普通 pycharm 路径
#data = YamlOperation("../Data/data.yaml")

# Case1
class TestCase:

    @pytest.fixture(scope="function",autouse=True)
    def delete_register(self):
        '''前置操作，删除注册的数据'''
        db_cnf = data.DB
        db = DbMysql(db_cnf)
        inv_email = '"' + data.Invitaion__bus_email.email1 + data.Email_type.snapmail + '"'
        operation_email='"' + data.Bussiness_acc.Admin_email + '"'
        print("收到邀请的用户"+inv_email)
        sql1 = 'DELETE FROM business_users where email=' + inv_email;
        sql2 = 'DELETE FROM business_user_roles where user_id = ( SELECT id FROM business_users where email='+inv_email+')';
        sql3 = 'DELETE FROM business_users where email=' + inv_email;
        sql4 = 'DELETE FROM invitation_account WHERE email='+inv_email+' AND business_company_id =(SELECT business_company_id FROM business_users WHERE email='+operation_email+')';

        db.execute(sql1)
        db.execute(sql2)
        db.execute(sql3)
        db.execute(sql4)
        db.close()
        print("数据初始化成功！  ！")

    @pytest.fixture(scope='function', autouse=True)
    @allure.feature('LOGIN_')
    def test_login(self, drivers):#登录

        page_ = Login_page(drivers)

        page_.open(data.Environment.url_qa)
        page_.email_input.send_keys(data.Bussiness_acc.Admin_email)
        page_.password_input.send_keys(data.Bussiness_acc.Admin_pwd)
        page_.login_button.click()

    @allure.feature('Verify that the status for Connection case is displayed correctly.')
    @pytest.mark.skip()
    def test_ST030(self, drivers):
        pass

    @pytest.mark.skip()
    def test_ST031(self, drivers):
        pass


    @allure.story("FREE businsee user Resigter")
    def test_T15_RegisterWeb(self,drivers):
        page_ = invitation_page(drivers)
        with allure.step("open invitation page"):
            page_.system_mune.click()
            page_.invitation_mune.click()
            sleep(3)

            with allure.step("invite ar_fst_email bus free user"):
                page_.create_button.click()
                #邮箱拼接
                page_.free_email.send_keys(data.Invitaion__bus_email.email1+data.Email_type.snapmail)
                sleep(3)
                page_.select_role.click()
                page_.create_bus.click()
                sleep(3)

            with allure.step("logout this user"):
                     #调用登出子脚本
                    subscript_p = subscript(drivers)

                    subscript_p.logout_bus_portal()

                    sleep(3)
                    with allure.step("open test email mail"):

                        new_window = 'window.open("{}")'.format(data.Environment.test_mail)  # js函数，此方法适用于所有的浏览器
                        page_.execute_script(new_window)
                        sleep(5)
                        page_.switch_to_window(1)

                        page_.add_email_button.click()
                        page_.input_email.clear()
                        page_.input_email.send_keys(data.Invitaion__bus_email.email1)
                        page_.confirm_emil_btn.click()

                        page_.invite_title.click()
                        sleep(3)

                        page_.switch_to_frame(1)# 切入iframe 切换到第二个子类frame-通过索引切换
                        page_.join_v8_link.click()
                        sleep(3)
                        page_.switch_to_parent_frame()# 切出iframe
                        page_.switch_to_window(-1) #最新的标签页
                        sleep(3)
                        with allure.step("regristion email mail"):
                            bus_email=data.Invitaion__bus_email.email1+data.Email_type.snapmail
                            print(page_.you_email.get_attribute('value'))

                            sleep(3)
                            #此处定位的为input输入框 用get_attribute 取获取value

                            assert page_.you_email.get_attribute('value')==bus_email
                            page_.your_password.send_keys(data.Invitaion__bus_email.password)
                            page_.confirm_password.send_keys(data.Invitaion__bus_email.password)
                            page_.next_button.is_enabled()
                            page_.next_button.click()
                            sleep(3)
                            with allure.step("find email verfiy code"):
                                page_.switch_to_window(-2)
                                page_.back_button.click()
                                sleep(10) #refash
                                page_.r_fst_email.click()
                                #切入frame
                                page_.switch_to_frame(1)
                                sleep(2)
                                '''
                                # 方法一 text() 结尾则由于XPath表达式以text（）结尾，因此解析为文本容器，而不是HTML元素（或列表）,
                                    使用完整的 xpath路径 利用 .text/get_attribute('textContent')[被隐藏可以使用这个]来提取文本
                                # 方法二 element = driver.find_element_by_css_selector('h1.ng-binding.ng-scope')
                                     text = driver.execute_script("return arguments[0].childNodes[0].textContent", element);
                                      print(text.strip())
                                '''
                                print(page_.text_email.get_attribute('textContent'))
                                sleep(2)
                                page_.switch_to_parent_frame()#切出
                                page_.switch_to_window(-1)
                                sleep(3)
                                page_.code_inp.send_keys(data.Verfiy_code.email_code)
                                page_.next_.click()
                                page_.accept_but.click()# s生成账号 成功
                                sleep(3)
                                page_.accept_but.click()
                                sleep(3)
                                with allure.step("输入受邀请人个人信息"):
                                    pro_email_check_infro=subscript_p.User_Profile(1,data.Invitaion__bus_email.email1,
                                                             None,data.Email_type.snapmail,data.Invitaion__bus_email.job)
                                    assert pro_email_check_infro[0]==bus_email
                                    print("创建新增business用户成功！")





















if __name__ == '__main__':
    # os.chdir(os.path.abspath('..')+'./venv./test_demo')
    # pytest.main(['-v','--alluredir=report/ST_jsonfile','smoke_test.py'])
    pytest.main(["-v", "--alluredir", "temp", '../test_demo/smoke_test.py'])
    # pytest.main(["-v", "-s", "--alluredir", "../temp", '../test_demo/smoke_test.py'])

    # os.system("allure generate ../temp -o ../report --clean")
    os.system("allure generate ./temp -o ./report --clean")
    # pytest - -alluredir = allure - results - -clean - alluredir

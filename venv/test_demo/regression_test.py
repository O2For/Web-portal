import os
import sys
#校验路径
sys.path.append(os.getcwd())
from selenium import webdriver
#POM
from PageObject.login_page import Login_page
from PageObject.customer_login import customer_login_page
from PageObject.subscript import subscript

from time import sleep
import pytest
import allure
from conftest import drivers
import re
# DBsql
from Common.db_server import DbMysql

# 数据准备导入路径
from Common.config import YamlOperation
#上jenkins要注释
os.chdir(os.path.abspath('..') + '/Data')
# 读取yaml数据文件
data = YamlOperation(os.getcwd() + "\data.yaml")

class TestCase:

    @pytest.fixture(scope="function", autouse=True)
    def delete_register(self):
        '''前置操作，删除注册的数据'''
        db_cnf = data.DB
        db = DbMysql(db_cnf)
        inv_email = '"' + data.indi_user_infor.ind_email +'"'
        print("收到邀请的用户" + inv_email)
        sql1 = 'DELETE FROM customer_user where email=' + inv_email;

        db.execute(sql1)
        db.close()
        print("数据初始化成功！  ！")
    @allure.story("Individual Sign up")
    @pytest.mark.skip()
    def test_T46_RegisterCustomer(self,drivers):
        cut = customer_login_page(drivers)
        cut.open(data.Environment.url_cur_uat);sleep(3)
        with allure.step("注册email"):
            cut.sign_up.click()
            cut.email.send_keys(data.indi_user_infor.ind_email)
            cut.inp_password.send_keys(data.indi_user_infor.password)
            cut.confirm_paw.send_keys(data.indi_user_infor.password)
            cut.accept_read.click()
            cut.confirm_btu.click();sleep(3)
            cut.code_input.send_keys(data.Verfiy_code.email_code)
            cut.confirm_btu.click();sleep(3)
            cut.role_ind.click();sleep(3)
            cut.fst_n.send_keys(data.indi_user_infor.fst)
            cut.lst_n.send_keys(data.indi_user_infor.lst)
            cut.confirm_btu.click();sleep(3)



    @allure.story("Individual Login in")
    @pytest.mark.parametrize("email,password",[(data.indi_user_infor.ind_email,data.indi_user_infor.password)])
    def test_T46_Login(self,drivers,email,password):

        cut = customer_login_page(drivers)
        cut.open(data.Environment.url_cur_uat);sleep(5)
        cut.email.send_keys(email)
        cut.password.send_keys(password)
        cut.login.click();sleep(3)




if __name__ == '__main__':
    pytest.main(["-vs","--alluredir", "reg_temp", '../test_demo/regression_test.py'])
    os.system("allure generate ./reg_temp -o ./reg_report --clean")


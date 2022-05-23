import os
import sys
sys.path.append(os.getcwd())
print(sys.path.append(os.getcwd()))
from selenium import webdriver

from time import sleep
import pytest
import allure
import re

#数据准备导入路径
from Common.config import YamlOperation

#os.chdir(os.path.abspath('..') + '/Data')
    #读取yaml数据文件
data = YamlOperation(os.getcwd() + "\Data\data.yaml")
#data = YamlOperation("../Data/data.yaml")

#Case1
class TestCase:

    @pytest.fixture(scope='function', autouse=True)
    @allure.feature('LOGIN_')
    def test_login(self,drivers):
        from PageObject.login_page import Login_page
        page=Login_page(drivers)

        page.open(data.Environment.url_qa)
        page.email_input.send_keys(data.Bussiness_acc.Admin_email)
        page.password_input.send_keys(data.Bussiness_acc.Admin_pwd)
        page.login_button.click()


    @allure.feature('Verify that the status for Connection '
                    'case is displayed correctly.')
    def test_ST030(self,drivers):
        pass
    def test_ST031(self,drivers):
        pass
if __name__ == '__main__':
    #os.chdir(os.path.abspath('..')+'./venv./test_demo')
    #pytest.main(['-v','--alluredir=report/ST_jsonfile','smoke_test.py'])
    pytest.main(["-v", "-s", "--alluredir", "temp",'./test_demo/smoke_test.py'])
    #pytest.main(["-v", "-s", "--alluredir", "../temp", '../test_demo/smoke_test.py'])

    #os.system("allure generate ../temp -o ../report --clean")
    os.system("allure generate ./temp -o ./report --clean")
    #pytest - -alluredir = allure - results - -clean - alluredir
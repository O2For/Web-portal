from selenium import webdriver

from time import sleep
import pytest
import allure
import re
import os
#数据准备导入路径
os.chdir(os.path.abspath('..') + '/Data')
    #读取yaml数据文件


#Case1
class TestCase:
    from Common.config import YamlOperation
    data = YamlOperation(os.getcwd() + "/data.yaml")
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
    os.chdir(os.path.abspath('..')+'/test_demo')
    pytest.main(["-v", "-s", "--alluredir", "temp",'smoke_test.py'])
    os.system("allure generate ./temp -o ./report --clean")
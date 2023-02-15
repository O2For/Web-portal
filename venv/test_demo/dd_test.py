import os
import sys
#校验路径
sys.path.append(os.getcwd())
print(sys.path.append(os.getcwd()))
from selenium import webdriver
#POM
from PageObject.test_page import StCv


#
from time import sleep
import pytest
import allure
from conftest import drivers
import re


# 数据准备导入路径
from Common.config import YamlOperation
#上jenkins要注释
os.chdir(os.path.abspath('..') + '/Data')
# 读取yaml数据文件
data = YamlOperation(os.getcwd() + "\data.yaml")

class TestCase:

    @allure.story("Individual Login in")
    @pytest.mark.parametrize("email,password", [(data.indi_user_infor.ind_email, data.indi_user_infor.password)])
    def test_T46_Login(self, drivers, email, password):
        cut = StCv(drivers)
        print(email)
        cut.open(data.Environment.url_cur_qa);
        sleep(5)
        #cut.email.send_keys(email)
        pp=cut.lo(email)




if __name__ == '__main__':
    pytest.main(["-vs","--alluredir", "reg_temp", '../test_demo/dd_test.py'])
    os.system("allure generate ./reg_temp -o ./reg_report --clean")
from time import sleep
import pytest
import allure
import re
from PageView.keybord_page import *

class TestCaes:

# coding:utf-8


    def test_key(self,drivers):
        i=0
        page = LOGIN(drivers)
        page.open("http://172.24.3.199:5001/ucase1")
        page.un.send_keys("jianghaodong")
        page.pw.send_keys("wsdjh")
        page.sign.click();sleep(3)
        #page1
        page.uscen.click()
        page.keyst.click();sleep(1)
        #page2
        while i<=99:
            ass0 = re.compile('输入如下的用户名\n')
            value0 = page.samply0.text
            text0 = ''.join(value0)
            trueass0 = ass0.sub('', text0, count=1)
            page.us_input.send_keys(trueass0)

            ass1 = re.compile('输入如下的密码\n')

            value1 = page.samply1.text
            text1 = ''.join(value1)
            trueass1 = ass1.sub('', text1, count=1)
            page.pw_input.send_keys(trueass1)
            page.num.click();
            sleep(1)
            i = i + 1

if __name__ == '__main__':
    pytest.main(['../test_demo/keyborad_test.py'])
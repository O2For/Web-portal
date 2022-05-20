from PageObject.baidu_page import BaiduPage
from selenium import webdriver
from time import sleep
import pytest
import allure

import re



class TestCase1:
    # @pytest.fixture(scope='function', autouse=True)
    # def open_baidu(self, drivers):
    #     """打开百度"""
    #     search = BaiduPage(drivers)
    #     search.open()

    @allure.feature('baidu_search')  # 在用例方法上添加即可
    def test_baidu(self, drivers):

        page = BaiduPage(drivers)
        # page.get("")
        with allure.step("第一步：open"):
            page.open("https://www.baidu.com")
        with allure.step("第二步：search"):
            page.input.send_keys("测试是否可以成功搜索")
            page.button.click()

            sleep(4)


            #此处不可以用get_title()此返回的是一个str类型
        assert page.get_title=="测试是否可以成功搜索_百度搜索"

    @pytest.mark.skip("此用例暂时不执行")
    def test_baidu2(self, drivers):
        page = BaiduPage(drivers)
        # page.get("")
        with allure.step("第一步：open"):
            page.open("https://www.baidu.com")
        with allure.step("第二步：search"):
            page.search_input("如何赚大钱")
            page.search_button()
            sleep(4)
            title = page.get_title()

        assert title == "如何赚大钱_百度搜索"

if __name__ == '__main__':
    pytest.main(["-s","--alluredir=report/jsonfile","test_bai.py","--clean-alluredir"])




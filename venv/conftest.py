import inspect

import pytest
from selenium import webdriver
import base64
import pytest
import allure
import os
from py.xml import html

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        options=webdriver.ChromeOptions()
        #options.add_argument('--incognito') #无痕
        driver = webdriver.Chrome(chrome_options=options)

        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver





@pytest.hookimpl(hookwrapper=True, tryfirst=True)
#此是用例最终结果的截图
def pytest_runtest_makereport(item, call):

    """
       获取每个用例状态的钩子函数
       :param item: 测试用例
       :param call: 测试步骤
       :return:
       #仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
       #然后执行  when="call" ，返回call测试用例的执行结果。
        # 添加allure报告截图
        # 如果当前webdriverr版本中有该方法，则使用
       """

    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        print('调用失败截图用具')
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step("当前case 失败截图"):
                allure.attach(driver.get_screenshot_as_png(), "case 失败截图", allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True)
def pytest_assume_fail(lineno, entry):
    file_name = os.getenv('PYTEST_CURRENT_TEST')

    for i in inspect.stack():
        #if file_name in i.filename:
            try:
                for k, v in i.frame.f_locals.items():
                    if hasattr(v, 'driver'):
                        with allure.step('断言失败'):
                            allure.attach(driver.get_screenshot_as_png(), "断言失败 截图", allure.attachment_type.PNG)

                        break

            except Exception:
                pass
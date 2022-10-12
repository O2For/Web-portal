import pytest
from selenium import webdriver
import base64
import pytest
import allure
from py.xml import html

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
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

             allure.attach(driver.get_screenshot_as_png(), "shithis a hh", allure.attachment_type.PNG)


'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)


def _capture_screenshot():
    """截图保存为base64"""
    now_time, screen_path = cm.screen_file
    driver.save_screenshot(screen_path)
    allure.attach.file(screen_path, "测试失败截图...{}".format(
        now_time), allure.attachment_type.PNG)
    with open(screen_path, 'rb') as f:
        imagebase64 = base64.b64encode(f.read())
    return imagebase64.decode()

'''
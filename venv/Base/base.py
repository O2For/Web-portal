from selenium import webdriver
import time



class BasePage(object):

    def __init__(self, driver=None):
        self.driver = driver

    def open(self, url=None):  # 如果url参数为None,则默认打开子类中定义的url
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)
        # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 显示等待
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    def by_name(self, name_):
        return self.driver.find_element_by_name(name_)

    def by_class(self, class_):

        return self.driver.find_element_by_class(class_)

    #
    # 定位元素方法
    def by_xpath(self, xpath_):
        return self.driver.find_element_by_xpath(xpath_)

        # 输入

    def send(self, selector, value):
        '''写'''
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(value)
        #  log1.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            # log1.error("Failed to select in input box with %s" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()

        except NameError as e:

            self.get_windows_img()

            # 点击元素

    def get_title(self):
        '''获取title'''
        title = self.driver.title
        return title

    def quit(self):
        self.driver.quit()

    # 获取页面text,仅使用XPath定
    def get_text(self, xpath):

        return self.by_xpath(xpath).text

class InvalidElementException(Exception):
    pass





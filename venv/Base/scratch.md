获取第三个a标签的下一个a标签："//a[@id=‘3’]/following-sibling::a[1]"

获取第三个a标签后面的第N个标签："//a[@id=‘3’]/following-sibling:: *[N]"

获取第三个a标签的上一个a标签："//a[@id=‘3’]re/preceding-sibling::a[1]"

获取第三个a标签的前面的第N个标签："//a[@id=‘3’]/preceding-sibling:: *[N]"

获取第三个a标签的父标签："//a[@id==‘3’]/…"




1 handles = driver.window_handles          #获取当前浏览器的所有窗口句柄
2 driver.switch_to.window(handles[-1])     #切换到最新打开的窗口
3 driver.switch_to.window(handles[-2])     #切换到倒数第二个打开的窗口
4 driver.switch_to.window(handles[0])      #切换到最开始打开的窗口

定义的脚本操作：
    def click_and_ctrl(self) -> None:
        """
        selenium API
        Holds down the left mouse button on an element.
        """
        elem = self.__get_element(self.k, self.v)
        ActionChains(Browser.driver).click(elem).key_up(Keys.CONTROL).perform()
        logging.info(f"✅ click_and_ctrl().")
        
        
定位取出文本：
xxxxxx.text  --适合不用xpath定位，

python 正则化：
            ass1 = re.compile('输入如下的密码\n') 需要删除/替换的文本

            value1 = page.samply1.text  整个文本
            text1 = ''.join(value1) 将文本变成字符串string
            trueass1 = ass1.sub('', text1, count=1) 开始替换，‘’表示需要替换/删除，count最大删除数量。
 Find 查找多个原元素方法      
    def find(self, context):
        for i in range(self.times):
            elems = Browser.driver.find_elements(*self.locator)
            if len(elems) == 0:
                sleep(1)
            else:
                break
        else:
            elems = []
            logging.info(f"✨ Find {len(elems)} elements through: {self.k}={self.v}. {self.desc}")
        return elems
        
        判断元素是否存在
     from selenium.common.exceptions import NoSuchElementException
     在element 里面修改
         def is_exist(self) -> bool:
        """Whether the element is visible to a user."""

        elem = Browser.driver.find_elements(by=self.k, value=self.v)
        if len(elem)==0:

            logging.info(f"❌ is_exist() -> {elem}. Eelement not exist")
            return False
        else:
            logging.info(f"√ is_exist() -> {elem}. Eelement exist")
            return True
            
            
                def scrollDownIntoView(self) -> None:
        """ 向下滚动至-元素可见"""
        elem = self.__get_element(self.k, self.v)
        Browser.driver.execute_script("arguments[0].scrollIntoView();", elem)

    def scrollUpIntoView(self) -> None:
        """ 向下滚动至-元素可见"""
        elem = self.__get_element(self.k, self.v)
        Browser.driver.execute_script("arguments[0].scrollIntoView(false);", elem)
            
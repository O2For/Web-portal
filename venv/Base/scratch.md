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

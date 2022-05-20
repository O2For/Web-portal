from  Base.base import BasePage

from poium import Page, Element

#进行页面各种操作与定位
# class BaiduPage(BasePage):
#     url= "https://www.baidu.com"
#     def search_input(self,search_key):
#         self.by_id("kw").send_keys(search_key)
#
#     def search_button(self):
#         self.by_id("su").click()

class BaiduPage(Page):
    input=Element(id_="kw",timeout=1,index=0,describe="search_box")
    button=Element(id_="su",timeout=1,index=0,describe="search_button")



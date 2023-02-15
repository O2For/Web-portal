from selenium import webdriver
import csv
import time
class page_id_find:
    '将页面id打印输入到指定csv当中'
    def __init__(self, driver):

        self.driver = driver


    '页面id检索'
    def filter_id(self):
        ids = self.driver.find_elements_by_xpath('//*[@id]')
        print("-------------读取当前页面成功---------------")
        id_list = []
        for ii in ids:
            # print ii.tag_name
            id_list.append(ii.get_attribute('id'))

            # print (ii.get_attribute('id'))   # id name as string
        add_id = [x for i, x in enumerate(id_list) if not x.find('icon') != -1]
        # write
        with open("C:\\Users\\jianghaodong\\Desktop\\id.csv", 'a', newline='') as f:
            try:
                return pickle.load(input_file)
            except EOFError:
                return None
        writer = csv.writer(f)
        writer.writerow(add_id)
        f.close()
        return print("------------成功写入当前页面id名称----------")









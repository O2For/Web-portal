import yaml
import os
import pandas as pd



import warnings
warnings.filterwarnings('ignore')


'''封装yaml 调用函数'''
class YamlOperation(dict):
    def __init__(self, file_path=None, content=None):
        super().__init__()

        if file_path is not None:
            with open(file_path, "r",encoding='utf-8')as file:


                #d加载数据 固定用法
                content = yaml.load(file, Loader=yaml.SafeLoader)
        # todo: 将yaml文件中读取的所有的key设置为类的属性
        content = content if content is not None else {}
        for key, value in content.items():
            # print(key)
            # print(value)
            if isinstance(value, dict):
                self[key] = YamlOperation(content=value)
            else:
                self[key] = value

    def __getattr__(self, key):
        """访问不存在的属性key时返回None"""
        return None

    def __setattr__(self, key, value):
        """设置实例属性值"""
        self[key] = value

    def __setitem__(self, key, value):
        """给self[key]赋值"""
        super().__setattr__(key, value)
        super().__setitem__(key, value)

    def __missing__(self, key):
        """访问的键key不存在时，返回None"""
        return None


'''封装文件路径查找 调用函数'''
class PathOperation(object):

    # 获得根路径
    def getRootPath(self):
        # 获取文件目录
        cur_path = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件的目录
        rootPath = cur_path[:cur_path.find('venv')] + 'venv'  # 获取根目录
        return rootPath

    # 从根目录下开始获取其他路径
    def getOtherPath(self,abspath: str):
        # 调用了上述获得项目根目录的方法
        rootPath = self.getRootPath()
        dataPath = os.path.abspath(rootPath + abspath)
        return dataPath


'''封装Excel 读取函数'''
class FileOperation(object):
    def getExecl(self):
        # TODO 首先导入xlrd这个库，后面会使用到xlrd中open_workbook和sheet_by_name方法
        # TODO 定义一个列表A待会储存读取的信息
        A = []
        #xx = xlrd.open_workbook(r"")
        root=PathOperation()
        excelpath=root.getOtherPath('/Data/try.xlsx')

        df = pd.read_excel(excelpath,sheet_name='STValue',header=0)
        # openpyxl只能处理 .xlsx 合适的表格

        data=dict(zip(df['data_name'],df['value']))

        return data

# if __name__ == '__main__':
#     import os
#
#     os.chdir(os.path.abspath('..') + '/Data')
#     #读取yaml数据文件
#     data = YamlOperation(os.getcwd() + "/data.yaml")
#     print(data.Environment)  # 输出：{'it': {'ot': 'daihua'}}
#     print(data['Environment'])  # 输出：{'it': {'ot': 'daihua'}}
#     print(data.get('Environment'))  # 输出：{'it': {'ot': 'daihua'}}
#     print(data.Environment.url_qa)  # 输出：daihua
#


# def func(nub,**kwargs):
#     """
#     **参数收集所有未匹配的关键字参数组成一个dict对象，局部变量kwargs指向此dict对象
#     """
#
#     if kwargs:
#
#         print("nub:")
#         print(nub)
#         print('kwargs = ', kwargs)
#         print(kwargs['cc'])
#     a=1
#     print(a)
#
#
# class Aasa(object):
#     def rr(self):
#         a=1
#         return "ccccc"
#
#     def aaaaaa(self):
#         if "xxx"==self.rr():
#             return print(1)
#         else: print(2)
#
#
# root=FileOperation()
# a=root.getExecl()
# print(a)


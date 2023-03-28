from Common.config import YamlOperation
import os


class GetData(object):
    '''静态方法是指类中无需实例参与即可调用的方法(不需要self参数)，
            在调用过程中，无需将类实例化，直接在类之后使用.号运算符调用方法。
            通常情况下，静态方法使用@staticmethod装饰器来声明。'''

    @staticmethod

    def TestData():
        '''通过yaml 读取数据'''
        try:
            Data=YamlOperation(os.path.dirname(os.path.abspath(__file__))+"\data.yaml")
            return Data
        except SyntaxError:
            print("<<< SyntaxError")
        except SystemExit:
            print("<<< NameError")
        except :
            print("GetData")


#
# da=GetData()
# a='BRD'
# data=da.TestData()
# print(dict(data.Photo_C))
# ditca=dict(data.Photo_C)
# print(ditca[a])

def abc():
    a=1
    b=2
    d=dict()


    return [a,b]
print(abc())
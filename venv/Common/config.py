import yaml
import os

# filePath=os.path.dirname(__file__)
# print(filePath)
# fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# print(fileNamePath)
# yamlPath = os.path.join(fileNamePath,'data.yaml')
# print(yamlPath)
# f= open(yamlPath,'r',encoding='utf-8')
#
# cont=f.read()
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


import os





#   ..返回上一级  . 当前文件夹


os.chdir(os.path.abspath('..')+'/Base')
path1= os.getcwd()
print(path1)

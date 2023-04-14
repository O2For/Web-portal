import os
import pytest

# coding=UTF8
# 当前路径(使用 abspath 方法可通过dos窗口执行)
current_path = os.path.dirname(os.path.abspath(__file__))
# json报告路径
json_report_path = os.path.join(current_path, 'report/json')
# html报告路径
html_report_path = os.path.join(current_path, 'report/html')

# 执行pytest下的用例并生成json文件
# pytest.main(['-vs','./test_demo/SmokeTesting_test.py', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
pytest.main(['-vs','./test_demo/SmokeTesting_test.py'])
# 把json文件转成html报告
# os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))


# if __name__ == '__main__':

    #pytest.main(['-vs','../test_demo/SmokeTesting_test.py', "--alluredir=./temp_st"])
    #pytest.main(['-vs', '../test_demo/SmokeTesting_test.py'])
    # pytest.main(["-vs", current_path+"\SmokeTesting_test.py"])


    #os.system("allure generate ./temp_st -o ./report_st --clean")

#上jenkns:pytest -vs ./test_demo/SmokeTesting_test.py

# '--workers=1', '--tests-per-worker=1'
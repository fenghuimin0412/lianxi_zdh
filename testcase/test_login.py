#pytest框架，模块名以test开头，类名以Test开头，方法以test开头
#1,测试用例数据的获取  2.登录接口发送请求
#导入写好的方法，业务层
from libs.login import Login
from utils.yamlControl import get_yaml_data
import pytest
import os

class TestLogin:
    @pytest.mark.parametrize('req_body,exp_data',get_yaml_data('../data/loginCase.yaml'))
    def test_login(self, req_body, exp_data):
        #1.调用登录接口
        #2.Login加个括号代表实例化
        #3.数据驱动
        res=Login().login(req_body)
        assert res.json().get('msg') == exp_data['msg']

if __name__ == '__main__':
    #pytest.main(["test_login.py", "-s", "--alluredir", "../report/tmp"])
    os.system("pytest test_login.py --alluredir=../report/tmp --clean-alluredir")
    #使用allure 产生报告
    os.system("allure serve ../report/tmp")
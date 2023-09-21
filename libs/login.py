from configs.env import URL
from data.data import test_data
import requests
import globalCommon


class Login:
    #token = None
    #封装登录接口
    def login(self,body_data):
        global token
        #1.请求的url
        url = f'{URL}/login' #格式化
        #2.请求头
        #3.请求bob
        resp = requests.post(url, json=body_data, verify=False)
        #data:使用场景---在请求头里面的type--表单格式 -表格格式
        #json:使用场景 ---在请求头里面的type ---json格式
        token = resp.headers.get('Authorization')
        globalCommon.session = token
        # print(globalCommon.session)
        return resp
if __name__ == '__main__':
    # test_data = {
    #     "username": "secadmin",
    #     "password": "IuJBziwHhjFiLxxV8Yb93vyfYUvOG6LXHMwf8mgQmcx/48J3XlcZ4ntcTSgy3N4dv9YZOnMkX6H0H+uzrwVezagnn+cUwx7UODm8kDdWr4I2An6XcWNAq7+UfIFWxYpHPdIJSNOybGvM4vbeYoHyTcnomo0ZkDie/F0ghAy/BKMUlT3+VSvM9yUOf5AiPv9LzOYj/PMZ4gALPBm6pobcIZqJgMQsUOftzOBe5Ja/tK/u27z28u8E0uEO1+sDnOkVCOkFnK9tdmHvAi5yHkv5CH5ep9sPhnEKKPVJPONjPoK5pu99u9H7HDoZrLfZKhMsmr/LFe2g/cUlKMHVQXUzbg=="
    # }
    #1.使用类去创建实例
    #2.NEW/INIT
    login = Login()
    #3.调用登录接口
    login.login(test_data)



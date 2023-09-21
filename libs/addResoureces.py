from configs.env import URL
import requests
import globalCommon
from libs.login import Login
from data.resData import res_data
from data.data import test_data

class addRes:
    def __init__(self):
        Login().login(test_data)
        self.headers = globalCommon.session
    def add_res(self, data) :
        # print(self.headers)
        url = f'{URL}/core/source/db/add'
        headers = {"Authorization": self.headers}
        res = requests.post(url, json=data, headers=headers, verify=False)
        return res

if __name__ == '__main__':
    addRes = addRes()
    addRes.add_res(res_data)
from libs.login import Login
from  data.data import test_data

class Token:
    token = ''
    def token(self):
        token = Login().login(test_data)
        return token


# -*- coding: utf-8 -*-
# //todo
# Created 16:05, 2018/7/6 by Yodes Yang
# password-storage-and-python-example: http://zhuoqiang.me/password-storage-and-python-example.html
# Hashing Strings with Python: https://www.pythoncentral.io/hashing-strings-with-python
# Python's safest method to store and retrieve passwords from a database:https://stackoverflow.com/questions/2572099
# /pythons-safest-method-to-store-and-retrieve-passwords-from-a-database
import os
from hashlib import sha256
from hmac import HMAC


class PasswordStorage(object):
    def __init__(self, password):
        self.password = password
        pass

    def encrypt(self, salt=None):
        if salt is None:
            salt = os.urandom(8)

        assert len(salt) == 8
        assert isinstance(salt, bytes)

        if isinstance(self.password, str):
            password = self.password.encode('UTF-8')
        else:
            password = self.password
        assert isinstance(password, bytes)

        result = password
        for i in range(10):
            result = HMAC(result, salt, sha256).digest()

        return salt + result

    def validate(self, hashed):
        return hashed == self.encrypt(hashed[:8])


if __name__ == '__main__':
    po = PasswordStorage('0220')
    print(po.encrypt())

    print(po.validate(po.encrypt()))

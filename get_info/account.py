#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
import shelve


class Account:
    def __init__(self):
        with shelve.open('./info') as db:
            self.username = db['self._username']
            self.password = db['self._password']

    def if_smart_account(self):
        while True:
            with shelve.open('./info') as db:
                account_repeat = input(f'是否使用账号{db["self._username"]}登录？回车默认，按1重新录入：\n')
                if account_repeat == '':
                    return self
                if account_repeat == '1':
                    return self.get_account_info()
                else:
                    print("是想使用新账号吗？按1重新输入哦")

    def get_account_info(self):
        with shelve.open('./info') as db:
            while True:
                self.username = input("请输入12306账号：")
                if self.username != '':
                    db['self._username'] = self.username
                    break
                else:
                    print("用户名不能为空")
            while True:
                self.password = getpass.getpass("请输入密码：")
                if self.password != '':
                    db['self._password'] = self.password
                    break
                else:
                    print('密码不能为空')
            return self


if __name__ == '__main__':
    account_info = Account().if_smart_account()
    print(account_info.username)
    print(account_info.password)

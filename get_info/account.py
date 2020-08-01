#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
import shelve


class Account:
    def __init__(self):
        with shelve.open('./info') as db:
            self.account_repeat = input(f'是否使用账号{db["self._username"]}登录？回车默认，按1重新录入')
            self.username = db['self._username']
            self.password = db['self._password']

    def get_account_info(self):
        while True:
            with shelve.open('./info') as db:
                if self.account_repeat == '':
                    return self
                if self.account_repeat == '1':
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
                else:
                    print("你很淘气哟")

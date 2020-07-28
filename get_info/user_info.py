#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass
import shelve

while True:
    with shelve.open('./info') as db:
        account_repeat = input(f'是否使用账号{db["username"]}登录？回车默认，按1重新录入')
        if account_repeat == '':
            username = db['username']
            password = db['password']
            break
        if account_repeat == '1':
            while True:
                username = input("请输入12306账号：")
                if username != '':
                    db['username'] = username
                    break
                else:
                    print("用户名不能为空")
            while True:
                password = getpass.getpass("请输入密码：")
                if password != '':
                    db['password'] = password
                    break
                else:
                    print('密码不能为空')
            break
        else:
            print("你很淘气哟")
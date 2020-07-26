#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass

username = input("请输入12306账号：")
password = getpass.getpass("请输入密码：")

while True:
    username = input("请输入12306账号：")
    if username != '':
        break
    else:
        print("用户名不能为空")
while True:
    password = getpass.getpass("请输入密码：")
    if password != '':
        break
    else:
        print('密码不能为空')
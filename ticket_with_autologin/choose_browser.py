#!/usr/bin/env python
# -*- coding: utf-8 -*-

driver_mark = input("请输入要使用的浏览器（默认为firefox）\n1：firefox\n2：chrome")
while True:
    if (driver_mark == '1') or (driver_mark == ""):
        driver = 'firefox'
        break
    if driver_mark == '2':
        driver = 'chrome'
        break
    else:
        print('咋个意思？')

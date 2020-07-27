#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

while True:
    with shelve.open('./info') as db:
        driver_mark = input(f"请输入要使用的浏览器（默认为{db['driver']}）\n1：firefox\n2：chrome\n")
        if driver_mark == '1':
            driver = 'firefox'
            db['driver'] = 'firefox'
            break
        elif driver_mark == '2':
            driver = 'chrome'
            db['driver'] = 'chrome'
            break
        elif driver_mark == '':
            driver = db['driver']
            break
        else:
            print('咋个意思？')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve


class Browser:
    def __init__(self):
        with shelve.open('./info') as db:
            self.driver = db['self._driver']

    def choose_browser(self):
        while True:
            with shelve.open('./info') as db:
                driver_mark = input(f"请输入要使用的浏览器（默认为{db['self._driver']}）：\n1：firefox\n2：chrome\n")
                if driver_mark == '1':
                    self.driver = 'firefox'
                    db['self._driver'] = 'firefox'
                    return self.driver
                elif driver_mark == '2':
                    self.driver = 'chrome'
                    db['self._driver'] = 'chrome'
                    return self.driver
                elif driver_mark == '':
                    return self.driver
                else:
                    print('咋个意思？')


if __name__ == '__main__':
    browser_info = Browser().choose_browser()
    print(browser_info)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

from get_info.info_to_login import Info_to_login
from page.auto_login import Auto_Login
from page.ticket import Ticket


class Tool:
    def __init__(self):
        with shelve.open('./info') as db:
            while True:
                option = input(f"***请填写信息开始抢票（直接回车读取上次记录）***\n"
                               f"\n您希望的抢票模式是（默认为{db['self.option']}）：\n"
                               "1：自动登录抢票模式\n"
                               "0：手工登录调试模式\n"
                               "注：调试模式仅支持Chrome，请确认已打开Chrome并进入调试模式。打开方法：命令行进入chrome.exe所在目录，"
                               "输入chrome --remote-debugging-port=9222，在浏览器中登录12306，登录成功保持浏览器打开即可。\n")
                if option == '1' or option == '0':
                    self.option = option
                    db['self.option'] = self.option
                    break
                elif option == '':
                    self.option = db['self.option']
                    break
                else:
                    print("要选疯狂模式吗？")
        if self.option == '1':
            self.info = Info_to_login().get_train().get_account().get_browser()

        elif self.option == '0':
            self.info = Info_to_login().get_train()
            print('***请稍后，即将开始抢票***！')

    def select_mode(self):
        if self.option == '1':
            return Auto_Login(self.info._browser).auto_login().type_info(self.info.start, self.info.end, self.info.date,
                                                                         self.info.time_period)
        elif self.option == '0':
            return Ticket().type_info(self.info.start, self.info.end, self.info.date, self.info.time_period)

    def brush(self, x: Ticket):
        has_available_train = x.query_ok().acquire_available_train(self.info.train)
        if has_available_train:
            while x.query_ok():
                get_ticket = x.get_ticket(self.info.seat)
                if get_ticket:
                    get_ticket.pay(self.info.who, self.info.seat)
                    return 0
                else:
                    continue
        else:
            print('查询的列车不存在，请检查相关信息。')

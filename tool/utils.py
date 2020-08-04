#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from page.auto_login import Auto_Login
from page.ticket import Ticket
from get_info.account import Account
from get_info.browser import Browser
from get_info.train import Train


class Utils:
    def __init__(self):
        self.start = ''
        self.end = ''
        self.date = ''
        self.train = ''
        self.time_period = ''
        self.who = ''
        self.seat = ''
        self._username = ''
        self._password = ''
        self._browser = ''
        self.option = ''

    def select_mode(self):
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
                    print("不要闹")
        if self.option == '1':
            return self.mode_1()
        elif self.option == '0':
            return self.mode_0()

    def mode_0(self):
        self.get_train()
        print('***请稍后，即将开始抢票！***')
        ticket = self.ticket_page()
        self.brush(ticket)

    def mode_1(self):
        self.get_train().get_account().get_browser()
        print('***请稍后，即将开始抢票！***')
        ticket = self.ticket_page()
        self.brush(ticket)

    def ticket_page(self):
        if self.option == '1':
            return Auto_Login(self._browser, self._username, self._password).auto_login().type_info(self.start,
                                                                                                    self.end,
                                                                                                    self.date,
                                                                                                    self.time_period)
        elif self.option == '0':
            return Ticket().type_info(self.start, self.end, self.date, self.time_period)

    def brush(self, x: Ticket):
        has_available_train = x.query_ok().acquire_available_train(self.train)
        print(f"查询到可用车次{has_available_train}")
        if has_available_train:
            while x.query_ok():
                get_ticket = x.get_ticket(self.seat)
                if get_ticket:
                    get_ticket.pay(self.who, self.seat)
                    return 0
                else:
                    continue
        else:
            print('查询的列车不存在，请检查相关信息。')

    def get_train(self):
        # get train info
        train_info = Train().if_smart_train()
        self.start = train_info.start
        self.end = train_info.end
        self.date = train_info.date
        self.train = train_info.train
        self.time_period = train_info.time_period
        self.who = train_info.who
        self.seat = train_info.seat
        return self

    def get_browser(self):
        # get browser info
        self._browser = Browser().choose_browser()
        return self

    def get_account(self):
        # init account info
        account_info = Account().if_smart_account()
        self._username = account_info.username
        self._password = account_info.password
        return self

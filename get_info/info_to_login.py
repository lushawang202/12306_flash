#!/usr/bin/env python
# -*- coding: utf-8 -*-
from get_info.account_info import Account_info
from get_info.browser import Browser
from get_info.Smart_train import Smart_train
from ticket_with_autologin.auto_login import Auto_Login


class Info_to_login:
    def __init__(self):
        train_info = Smart_train().if_smart_train()
        self.start = train_info.start
        self.end = train_info.end
        self.date = train_info.date
        self.train = train_info.train
        self.time_period = train_info.time_period
        self.who = train_info.who
        self.seat = train_info.seat
        get_account_info = Account_info().get_account_info()
        self._username = get_account_info.username
        self._password = get_account_info.password
        self._browser = Browser().choose_browser()

    def goto_login(self):
        print('请稍后，即将开始抢票！')
        return Auto_Login(self._browser, self._username, self._password)

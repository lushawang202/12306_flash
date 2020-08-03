#!/usr/bin/env python
# -*- coding: utf-8 -*-
from get_info.account import Account
from get_info.browser import Browser
from get_info.train import Train


class Info_to_login:
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
        print('***请稍后，即将开始抢票！***')
        return self

    def get_account(self):
        # init account info
        get_account_info = Account().if_smart_account()
        self._username = get_account_info.username
        self._password = get_account_info.password
        return self


if __name__ == '__main__':
    Info_to_login().get_train().get_account().get_browser()

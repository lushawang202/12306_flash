#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

# 自动登录，查票，买票，加浏览器选择

from ticket_with_autologin.auto_login import Auto_Login

if __name__ == '__main__':
    print('😊全自动抢票小助手为您服务！请填写信息开始抢票（直接回车表示默认）：')
    from common.query_info import *
    from ticket_with_autologin.choose_browser import *
    from ticket_with_autologin.user_info import *
    print('请稍后，即将开始抢票！')
    auto_login = Auto_Login(driver, username, password)
    auto_login.auto_login().check_ticket(start, end, date, time_period).buy_ticket(train).pay(who, seat)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page.ticket import Ticket
if __name__ == '__main__':
    print(
        '\n注：非自动登录只支持Chrome debug模式，请确认已打开Chrome调试模式。\n'
        '打开方法：命令行进入chrome.exe所在目录，'
        '输入chrome --remote-debugging-port=9222，在浏览器中登录12306，登录成功保持浏览器打开即可。'
        '\n请填写信息开始抢票（直接回车表示默认）。\n')
    from common.query_info import *

    ticket = Ticket()
    ticket.check_ticket(start, end, date, time_period).buy_ticket(train).pay(who, seat)

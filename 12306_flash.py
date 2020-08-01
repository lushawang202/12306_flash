#!/usr/bin/env python
# -*- coding: utf-8 -*-
from get_info.info_to_login import Info_to_login
from page.ticket import Ticket

if __name__ == '__main__':
    print('O(∩_∩)O全自动抢票小助手为您服务！请填写信息开始抢票（直接回车表示默认）。')
    print(
        '\n注：非自动登录只支持Chrome debug模式，请确认已打开Chrome调试模式。\n'
        '打开方法：命令行进入chrome.exe所在目录，'
        '输入chrome --remote-debugging-port=9222，在浏览器中登录12306，登录成功保持浏览器打开即可。'
        '\n请填写信息开始抢票（直接回车表示默认）。\n')

    info = Info_to_login()
    print('请稍后，即将开始抢票！')
    ready_to_ticket = Ticket().type_info(info.start, info.end, info.date, info.time_period)
    has_available_train = ready_to_ticket.query_ok().acquire_available_train(info.train)
    if has_available_train:
        while ready_to_ticket.query_ok():
            get_ticket = ready_to_ticket.get_ticket(info.seat)
            if get_ticket:
                get_ticket.pay(info.who, info.seat)
                break
            else:
                continue
    else:
        print('查询的列车不存在，请检查相关信息。')

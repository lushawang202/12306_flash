#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自动登录，查票，买票，加浏览器选择
from get_info.info_to_login import Info_to_login

if __name__ == '__main__':
    print('O(∩_∩)O全自动抢票小助手为您服务！请填写信息开始抢票（直接回车表示默认）。')
    info = Info_to_login().get_account()
    print('请稍后，即将开始抢票！')
    ready_to_ticket = info.goto_login().auto_login().type_info(info.start, info.end, info.date, info.time_period)
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

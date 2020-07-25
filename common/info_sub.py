#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


while True:
    date = time.strftime('%Y-%m-%d')
    start = input("从哪走呀？（默认宣化）：")
    if start == '':
        start = '宣化'
    end = input("到哪了？（默认北京）：")
    if end == '':
        end = '北京'
    date = input(f"哪天走？（默认{date}）：")
    if date == '':
        date = time.strftime('%Y-%m-%d')
    time_period_mark = input(
        "哪个时间段的？（默认00:00--24:00）\n"
        "1：00:00--06:00\n"
        "2：06:00--12:00\n"
        "3：12:00--18:00\n"
        "4：18:00--24:00")
    if time_period_mark == '1':
        time_period = '00:00--06:00'
    elif time_period_mark == '2':
        time_period = '06:00--12:00'
    elif time_period_mark == '3':
        time_period = '12:00--18:00'
    elif time_period_mark == '4':
        time_period = '18:00--24:00'
    else:
        time_period = '00:00--24:00'

    train = input("哪（几）个车？多个用空格隔开（默认为G7872）:")
    if train == '':
        train = 'G7872'
    who = input("谁坐呀？（默认姚继承）")
    if who == '':
        who = '姚继承'
    seat = input("什么坐席？（默认二等座）")
    if seat == '':
        seat = '二等座'
    flag = input(
        f"\n\n准备开抢！看看信息对不对⬇\n\n{date}\n起点：{start}\n终点：{end}\n车次：{train}\n"
        f"时间段：{time_period}\n姓名：{who}\n坐席：{seat}\n对按1，不对别按1：")
    if flag == '1':
        break







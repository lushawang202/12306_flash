#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import time

while True:
    with shelve.open('./info') as db:
        start = input(f"从哪走呀？（默认{db['start']}）：")
        end = input(f"到哪了？（默认{db['end']}）：")
        date = input(f"哪天走？（默认{db['date']}）：")
        time_period_mark = input(
            f"哪个时间段的？（默认{db['time_period']}）\n"
            "0: 00:00--24:00\n"
            "1：00:00--06:00\n"
            "2：06:00--12:00\n"
            "3：12:00--18:00\n"
            "4：18:00--24:00\n")
        if time_period_mark == '1':
            time_period = '00:00--06:00'
        elif time_period_mark == '2':
            time_period = '06:00--12:00'
        elif time_period_mark == '3':
            time_period = '12:00--18:00'
        elif time_period_mark == '4':
            time_period = '18:00--24:00'
        elif time_period_mark == '0':
            time_period = '00:00--24:00'
        else:
            time_period = ''
        train = input(f"哪（几）个车？多个用空格隔开（默认为{db['train']}）:")
        who = input(f"谁坐呀？（默认{db['who']}）")
        seat = input(f"什么坐席？（默认{db['seat']}）")
        info_list = ['start', 'end', 'date', 'time_period', 'train', 'who', 'seat']
        count = 0

        for i in info_list:
            count += 1
            if eval(i) == '':
                if count == 1:
                    start = db[i]
                elif count == 2:
                    end = db[i]
                elif count == 3:
                    date = db[i]
                elif count == 4:
                    time_period = db[i]
                elif count == 5:
                    train = db[i]
                elif count == 6:
                    who = db[i]
                else:
                    seat = db[i]
            else:
                db[i] = eval(i)

    flag = input(
        f"\n\n准备开抢！看看信息对不对⬇\n\n{date}\n起点：{start}\n终点：{end}\n车次：{train}\n"
        f"时间段：{time_period}\n姓名：{who}\n坐席：{seat}\n对按1，不对别按1：\n")
    if flag == '1':
        break

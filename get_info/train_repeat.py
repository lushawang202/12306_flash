#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

while True:
    repeat = input('是否一键读取上次信息？（是按1，不是别按1）')
    if repeat == '1':
        with shelve.open('./info') as db:
            start = db['start']
            end = db['end']
            date = db['date']
            train = db['train']
            time_period = db['time_period']
            who = db['who']
            seat = db['seat']
            driver = db['driver']
    else:
        from get_info.train_info import *
    flag = input(
        f"\n\n准备开抢！看看信息对不对⬇\n\n{date}\n起点：{start}\n终点：{end}\n车次：{train}\n"
        f"时间段：{time_period}\n姓名：{who}\n坐席：{seat}\n对按1，不对别按1：\n")
    if flag == '1':
        break

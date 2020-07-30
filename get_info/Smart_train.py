#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve


class Smart_train:
    def __init__(self):
        with shelve.open('./info') as db:
            self.start = db['self.start']
            self.end = db['self.end']
            self.date = db['self.date']
            self.train = db['self.train']
            self.time_period = db['self.time_period']
            self.who = db['self.who']
            self.seat = db['self.seat']
            self.smart_mark = input(f'是否一键读取上次信息？\n{self.date}\n起点：{self.start}\n'
                                    f'终点：{self.end}\n车次：{self.train}\n时间段：{self.time_period}\n'
                                    f'姓名：{self.who}\n坐席：{self.seat}\n回车默认，按1重新录入：')

    def if_smart_train(self):
        while True:
            if self.smart_mark == '':
                return self
            elif self.smart_mark == '1':
                return self.get_train_info()
            else:
                print('咦？手误了吗？')

    def get_train_info(self):
        while True:
            with shelve.open('./info') as db:
                self.start = input(f"从哪走呀？（默认{db['self.start']}）：")
                self.end = input(f"到哪了？（默认{db['self.end']}）：")
                self.date = input(f"哪天走？（默认{db['self.date']}）：")
                time_period_mark = input(
                    f"哪个时间段的？（默认{db['self.time_period']}）\n"
                    "0: 00:00--24:00\n"
                    "1：00:00--06:00\n"
                    "2：06:00--12:00\n"
                    "3：12:00--18:00\n"
                    "4：18:00--24:00\n：")
                if time_period_mark == '1':
                    self.time_period = '00:00--06:00'
                elif time_period_mark == '2':
                    self.time_period = '06:00--12:00'
                elif time_period_mark == '3':
                    self.time_period = '12:00--18:00'
                elif time_period_mark == '4':
                    self.time_period = '18:00--24:00'
                elif time_period_mark == '0':
                    self.time_period = '00:00--24:00'
                else:
                    self.time_period = '00:00--24:00'
                self.train = input(f"哪（几）个车？多个用空格隔开（默认为{db['self.train']}）:")
                self.who = input(f"谁坐呀？（默认{db['self.who']}）：")
                self.seat = input(f"什么坐席？（默认{db['self.seat']}）：")
                info_list = ['self.start', 'self.end', 'self.date', 'self.time_period', 'self.train', 'self.who', 'self.seat']
                count = 0

                for i in info_list:
                    count += 1
                    if eval(i) == '':
                        if count == 1:
                            self.start = db[i]
                        elif count == 2:
                            self.end = db[i]
                        elif count == 3:
                            self.date = db[i]
                        elif count == 4:
                            self.time_period = db[i]
                        elif count == 5:
                            self.train = db[i]
                        elif count == 6:
                            self.who = db[i]
                        else:
                            self.seat = db[i]
                    else:
                        db[i] = eval(i)
            flag = input(
                f'准备开抢！看看信息对不对⬇\n{self.date}\n起点：{self.start}\n终点：{self.end}\n车次：{self.train}\n'
                f'时间段：{self.time_period}\n姓名：{self.who}\n坐席：{self.seat}\n对按1，不对别按1：')
            if flag == '1':
                return self

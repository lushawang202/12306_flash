#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 自动登录，查票，买票，加浏览器选择
from tool.auto_go import Tool

if __name__ == '__main__':
    print('O(∩_∩)O全自动抢票小助手为您服务！请填写信息开始抢票（直接回车表示默认）。\n')
    auto_go = Tool()
    mode = auto_go.select_mode()
    auto_go.brush(mode)

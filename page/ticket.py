#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base import Base
from page.pay import Pay


class Ticket(Base):
    _url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
    available_trains = []

    # 录入查询信息
    def type_info(self, start, end, date, time_period):
        self.wait_ele_clickable(5, (By.ID, 'wf'))
        # 设置from_city to_city date time
        from_city = self.find(By.ID, 'fromStationText')
        # 火狐浏览器需要两次输入才生效
        from_city.click()
        from_city.send_keys(f'{start}\n')
        from_city.click()
        from_city.send_keys(f'{start}\n')
        to_city = self.find(By.ID, 'toStationText')
        to_city.click()
        to_city.send_keys(f'{end}\n')
        # action_chains().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.execute_script(
            f'a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="{date}"')
        time_period_ele = self.find(By.ID, 'cc_start_time')
        Select(time_period_ele).select_by_visible_text(f'{time_period}')
        return self

    def query_ok(self):
        self.implicitly_wait(3)
        while True:
            self.wait_ele_clickable(5, (By.CSS_SELECTOR, '#wf'))
            self.find(By.ID, 'query_ticket').click()
            if self.find(By.ID, 'wf').is_enabled():
                return self

    # 获得可用车次
    def acquire_available_train(self, trains):
        self.implicitly_wait(0.5)
        if self.find(By.XPATH, '//*[contains(text(),"很抱歉，按您的查询条件，当前未找到")]').is_displayed():
            print('没有找到可用列车')
            self.screen_shot('./获取车次异常.png')
            return False
        else:
            trains = [x for x in trains.split(' ')]
            for train in trains:
                if self.finds(By.XPATH, f'//*[text()="{train}"]'):
                    self.available_trains.append(train)
                else:
                    continue
            if len(self.available_trains) > 0:
                print(f"查询到可用车次：{self.available_trains}，刷票中...")
                return True
            else:
                return False

    def get_ticket(self, seat):
        seat_number = None
        for train in self.available_trains:
            if seat == '二等座':
                seat_number = 4
            elif seat == '一等座':
                seat_number = 3
            elif seat == '软卧':
                seat_number = 6
            elif seat == '硬卧':
                seat_number = 8
            elif seat == '软座':
                seat_number = 9
            elif seat == '硬座':
                seat_number = 10
            rest = self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[{seat_number}]').text
            if rest != '无' and rest != '候补' and rest != '--':
                try:
                    print(f"{train}余票：{rest}")
                    self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[last()]').click()
                    return self.goto_pay()
                except Exception:
                    self.screen_shot('./订票异常.png')
                    return False
            else:
                return False

    def goto_pay(self):
        while True:
            self.implicitly_wait(0.1)
            if self.finds(By.XPATH, '//div[contains(text(),"您选择的列车距开车时间很近了")]'):
                self.wait_ele_clickable(5, (By.ID, 'qd_closeDefaultWarningWindowDialog_id'))
                self.find(By.ID, 'qd_closeDefaultWarningWindowDialog_id').click()
                return Pay(self._driver)
            elif self.finds(By.ID, 'submitOrder_id'):
                return Pay(self._driver)
            elif self.finds(By.XPATH, '//*[contains(text(), "当前时间不可以订票")]'):
                print('抢票失败：查询到可用车票，但是当前时间不可以订票。')
                return False
            elif self.finds(By.ID, 'content_defaultwarningAlert_hearder'):
                print('无法订票，因为有未处理的订单')
                raise Exception
            elif self.finds(By.CSS_SELECTOR, '.modal-login'):
                self.refresh()
                # from ticket_with_autologin.auto_login import Auto_Login
                # Auto_Login(self._driver).auto_login()
                return self.goto_pay()
            else:
                continue

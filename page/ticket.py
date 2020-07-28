#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winsound
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base import Base
from page.pay import Pay


class Ticket(Base):
    _url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
    available_trains = []

    def check_ticket(self, start, end, date, time_period):
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
        self.find(By.ID, 'query_ticket').click()
        return self

    # 获得可用车次
    def acquire_available_train(self, trains):
        trains = [x for x in trains.split(' ')]
        self.implicitly_wait(0.5)
        while True:
            self.wait_to_click(3, (By.ID, 'wf'))
            if self.finds(By.ID, 'float'):
                for train in trains:
                    if self.finds(By.XPATH, f'//*[text()="{train}"]'):
                        self.available_trains.append(train)
                        print(self.available_trains)
                self.implicitly_wait(8)
                break
            elif self.find(By.XPATH, '//*[contains(text(),"稍后再试")]').is_displayed():
                self.refresh()
            else:
                self.screen_shot('./获取车次异常.png')
                print('获取车次异常')
                self.refresh()

    def buy_ticket(self, trains):
        self.acquire_available_train(trains)
        if len(self.available_trains) == 0:
            print('\n我不得不退出，因为当前搜索没有你说的车。')
            raise Exception
        else:
            while True:
                for train in self.available_trains:
                    if self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[4]').text != '候补':
                        self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[last()]').click()
                        self.implicitly_wait(0.3)
                        if self.finds(By.XPATH, '//*[contains(text(), "当前时间不可以订票")]'):
                            print('抢票失败：当前时间不可以订票')
                            raise Exception
                        elif self.finds(By.XPATH, '//div[contains(text(),"您选择的列车距开车时间很近了")]'):
                            self.find(By.ID, 'qd_closeDefaultWarningWindowDialog_id').click()
                        else:
                            if self.find(By.ID, 'submitOrder_id').is_displayed():
                                winsound.Beep(600, 1000)
                                print("恭喜小主抢到啦！快去付款吧~")
                                return Pay(self._driver)
                            else:
                                self.screen_shot('./订票跳转失败.png')
                self.find(By.ID, 'query_ticket').click()


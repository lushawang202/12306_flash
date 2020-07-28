#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winsound

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from page.base import Base
from page.pay import Pay


class Ticket(Base):
    _url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'

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
        # action_chains = ActionChains(self._driver)
        # action_chains.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self._driver.execute_script(
            f'a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="{date}"')
        time_period_ele = self.find(By.ID, 'cc_start_time')
        Select(time_period_ele).select_by_visible_text(f'{time_period}')
        self.find(By.ID, 'query_ticket').click()
        return self

    def buy_ticket(self, trains):
        trains = [x for x in trains.split(' ')]
        while True:
            WebDriverWait(self._driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, 'wf')))
            count = 0
            flag = 1
            for train in trains:
                self._driver.implicitly_wait(0.5)
                if self.finds(By.XPATH, f'//a[text()="{train}"]'):
                    flag = 0
                    if self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[4]').text != '候补':
                        self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[last()]').click()
                        try:
                            self._driver.implicitly_wait(8)
                            self.find(By.ID, 'submitOrder_id')
                            winsound.Beep(600, 1000)
                            print("恭喜小主抢到啦！快去付款吧~")
                            return Pay(self._driver)
                        except NoSuchElementException:
                            print('抢票失败：当前时间不可以订票')
                            raise Exception

                elif flag:
                    if self.find(By.XPATH, '//*[contains(text(),"稍后再试")]').is_displayed():
                        break
                    else:
                        count += 1
                        if count == len(trains):
                            print('\n我不想再继续了，因为当前搜索没有你说的车。')
                            raise Exception

            self.find(By.ID, 'query_ticket').click()

    def quit(self):
        self._driver.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        self.click_till_see(By.ID, 'query_ticket', By.CSS_SELECTOR, '.start-s')
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

    def get_ticket(self):
        for train in self.available_trains:
            rest = self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[4]').text
            try:
                if rest != '候补':
                    print(f"{train}[0]余票：{rest}")
                    self.find(By.XPATH, f'//a[text()="{train}"]/../../../../../td[last()]').click()
                    self.wait_ele_not_clickable(10, (By.LINK_TEXT, '我的12306'))
                    self.implicitly_wait(0.2)
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
                    else:
                        raise Exception
                else:
                    return False
            except Exception:
                self.screen_shot('./订票跳转失败.png')
                print("抢票失败，错误截图已保存为：订票跳转失败.png")
                raise Exception



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winsound
from selenium.webdriver.common.by import By
from page.base import Base


class Pay(Base):
    def pay(self, name, seat):
        try:
            self.wait_ele_clickable(10, (By.CSS_SELECTOR, '#normalPassenger_0'))
            self.find(By.XPATH, f'//*[text()="{name}"]/../input').click()
            select = self.find(By.ID, 'seatType_1')
            select.find_element(By.XPATH, f'//option[contains(text(), "{seat}")]').click()
            self.wait_ele_clickable(5, (By.ID, 'submitOrder_id'))
            self.find(By.ID, 'submitOrder_id').click()
            self.wait_ele_clickable(5, (By.ID, 'qr_submit_id'))
            self.find(By.ID, 'qr_submit_id').click()
            # self.click_till_see(By.ID, 'qr_submit_id', By.XPATH, '//*[contains(text(),"请稍等")]')
            self.implicitly_wait(0.1)
            while True:
                if self.finds(By.LINK_TEXT, '失败!'):
                    self.screen_shot('./订票失败.png')
                    print("订票失败，详情请查看：订票失败.png")
                    return False
                elif self.finds(By.CSS_SELECTOR, '.pay-tips'):
                    winsound.Beep(600, 3000)
                    print('恭喜小主抢到票啦！坐席已被锁定10分钟，快去付款吧~')
                    return True
                else:
                    continue
        except Exception:
            print('订票异常')
            self.screen_shot('./订票异常.png')
            raise Exception

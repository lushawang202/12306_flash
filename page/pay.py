#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winsound

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from page.base import Base


class Pay(Base):
    def pay(self, name, seat):
        while True:
            try:
                # self.find(By.ID, 'quickQueryPassenger_id').send_keys(name)
                self.find(By.XPATH, f'//*[text()="{name}"]/../input').click()
                select = self.find(By.ID, 'seatType_1')
                select.find_element(By.XPATH, f'//option[contains(text(), "{seat}")]').click()
                self.find(By.ID, 'submitOrder_id').click()
                self.find(By.ID, 'qr_submit_id').click()
                break
            except NoSuchElementException:
                if self.finds(By.XPATH, '//*[text(),"确定"]'):
                    self.find(By.XPATH, '//*[text(),"确定"]').click()
                else:
                    self._driver.save_screenshot('./提交失败.png')
        while True:
            winsound.Beep(600, 1000)

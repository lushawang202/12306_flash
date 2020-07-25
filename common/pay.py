#!/usr/bin/env python
# -*- coding: utf-8 -*-

import winsound

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base import Base


class Pay(Base):
    def pay(self, name, seat):
        # self.find(By.ID, 'quickQueryPassenger_id').send_keys(name)
        self.find(By.XPATH, f'//*[text()="{name}"]/../input').click()
        select = self.find(By.ID, 'seatType_1')
        select.find_element(By.XPATH, f'//option[contains(text(), "{seat}")]').click()
        self.find(By.ID, 'submitOrder_id').click()
        while True:
            winsound.Beep(600, 1000)

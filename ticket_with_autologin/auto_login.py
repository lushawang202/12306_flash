# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import re
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base import Base
from page.ticket import Ticket


class Auto_Login(Base):
    _url = 'https://kyfw.12306.cn/otn/resources/login.html'
    _coordinate = [[-105, -20], [-35, -20], [40, -20], [110, -20], [-105, 50], [-35, 50], [40, 50], [110, 50]]

    def __init__(self, driver, username, password):
        super().__init__(driver)
        self._username = username
        self._password = password

    def auto_login(self):
        # 用户名、密码输入
        WebDriverWait(self._driver, 3).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, '账号登录')))
        self.find(By.LINK_TEXT, '账号登录').click()

        self.find(By.ID, 'J-userName').send_keys(f'{self._username}')
        self.find(By.ID, 'J-password').send_keys(f'{self._password}')

        # def img_verify(self):
        while True:
            WebDriverWait(self._driver, 10).until(
                expected_conditions.invisibility_of_element((By.CSS_SELECTOR, '.lgcode-loading')))
            img_ele = self.find(By.ID, 'J-loginImg')
            base64_str = img_ele.get_attribute("src").split(",")[-1]
            imgdata = base64.b64decode(base64_str)
            with open('verify.jpg', 'wb') as file:
                file.write(imgdata)
            self.img_ele = img_ele
            # def getVerifyResult(self):
            url = "http://littlebigluo.qicp.net:47720/"
            response = requests.request("POST", url, data={"type": "1"}, files={
                'pic_xxfile': open('verify.jpg', 'rb')})
            result = []
            # print(response.text)
            try:
                for i in re.findall("<B>(.*)</B>", response.text)[0].split(" "):
                    result.append(int(i) - 1)
            except Exception as e:
                print("图像处理服务器繁忙，即将尝试")
                continue
            self.result = result
            # def moveAndClick(self):
            self.action = ActionChains(self._driver)
            for i in self.result:
                self.action.move_to_element(self.img_ele).move_by_offset(self._coordinate[i][0],
                                                                         self._coordinate[i][1]).click()
            self.action.perform()
            self.find(By.ID, 'J-login').click()
            if self.finds(By.ID, 'nc_1_n1z'):
                break
            elif self.finds(By.XPATH, '//*[contains(text(),"密码长度不能少于6位")]'):
                print("密码长度不能少于6位！")
                self._driver.save_screenshot('./密码太短.png')
                raise Exception
            else:
                print('验证码选择失败，即将重试')
                self.find(By.CSS_SELECTOR, '.lgcode-refresh').click()

        # def slide(self):
        while True:
            try:
                action_chains = ActionChains(self._driver)
                start = self.find(By.ID, 'nc_1_n1z')
                action_chains.click_and_hold(start).move_by_offset(340, 0).pause(0.1).release().perform()
                self._driver.implicitly_wait(2)
                if self.finds(By.LINK_TEXT, '刷新'):
                    self.find(By.LINK_TEXT, '刷新').click()
                elif self.finds(By.LINK_TEXT, '确定'):
                    self.find(By.LINK_TEXT, '确定').click()
                    break
                elif self.finds(By.XPATH, '//*[text()="个人中心"]'):
                    break
                elif self.finds(By.XPATH, '//*[contains(text(),"密码输入错误")]'):
                    print('密码输入错误。')
                    raise Exception
                else:
                    raise Exception
                self._driver.implicitly_wait(8)
            except Exception:
                self._driver.save_screenshot('./验证失败.png')
                print('滚动条验证失败')
                raise Exception
        return Ticket(self._driver)

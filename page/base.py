#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _driver = None
    _url = ""

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
        elif driver == 'firefox':
            self._driver = webdriver.Firefox()
        elif driver == 'chrome':
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._url != "":
            self._driver.get(self._url)
        self._driver.maximize_window()
        self._driver.implicitly_wait(8)

    def find(self, by, value):
        return self._driver.find_element(by, value)

    def finds(self, by, value):
        return self._driver.find_elements(by, value)

    def action_chains(self):
        return ActionChains(self._driver)

    def execute_script(self, script):
        self._driver.execute_script(script)

    def implicitly_wait(self, time):
        self._driver.implicitly_wait(time)

    def click_till_jump(self, by, locator):
        while True:
            self.find(by, locator).click()
            if len(self.finds(by, locator)) == 0:
                break

    def wait_to_click(self, time: float, locator):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def wait_to_invisible(self, time, locator):
        WebDriverWait(self._driver, time).until(expected_conditions.invisibility_of_element(locator))

    def refresh(self):
        self._driver.refresh()

    def screen_shot(self, filename):
        self._driver.save_screenshot(filename)

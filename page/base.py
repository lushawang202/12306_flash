#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


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
        self._driver.implicitly_wait(5)

    def find(self, by, value):
        return self._driver.find_element(by, value)

    def finds(self, by, value):
        return self._driver.find_elements(by, value)

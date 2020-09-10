#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://baidu.com')
driver.find_element_by_id("kw").send_keys('大')
driver.find_element_by_name("wd").send_keys('道')
driver.find_element_by_class_name("s_ipt").send_keys("至")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("简")
driver.find_element_by_xpath("//form[@name='f']/span/input").send_keys("是")
driver.find_element_by_css_selector("input#kw").send_keys("嘛")      #在css定位中，id简写用 # 来表式，class属性简写用 . 来表式。
driver.find_element_by_css_selector("form#form>span>input").send_keys("呀")      #在css定位中，层级关系用 > 来表式，有时为了简洁，也可以直接替换成空格
time.sleep(5)
driver.quit()
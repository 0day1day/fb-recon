# !/usr/bin/env python

import httplib2
import json

from getpass import getpass
from selenium import webdriver

def login(driver):
    driver.get('https://www.facebook.com/')
    assert "Welcome to Facebook" in driver.title
    creds = getCredentials()
    driver.find_element_by_id('email').send_keys(creds[0])
    driver.find_element_by_id('pass').send_keys(creds[1])
    driver.find_element_by_id('loginbutton').click()

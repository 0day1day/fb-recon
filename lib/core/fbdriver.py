# !/usr/bin/env python

import httplib2
import json

from getpass import getpass
from selenium import webdriver

class Fbdriver(webdriver):
    def __init__(self):
        
        
    def login(driver):
        this.get('https://www.facebook.com/')
        assert "Welcome to Facebook" in this.title
        creds = getCredentials()
        this.find_element_by_id('email').send_keys(creds[0])
        this.find_element_by_id('pass').send_keys(creds[1])
        this.find_element_by_id('loginbutton').click()

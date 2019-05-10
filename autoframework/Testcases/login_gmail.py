from selenium import webdriver
from Libraries.web_operations import *
from common_library import *
from login_gmail_elements import *
import time

# Parese json file
def test_login_gmail():

    '''
    Author : Mubarak
    Created Date   : 08/May/2019
    updated Date   : 08/May/2019
    Check gmail login page is working or not properly
    '''
    # Parse json file
    jdata = parse_json(r'gmail_config.json')
    # Open a chrome browser to login gmail
    driver = open_chrome_browser(jdata['url'])
    enter_text_by_id(driver,uname_id,jdata['uname'])
    click_element_by_xpath(driver, uname_next_xpath)
    enter_text_by_name(driver, passw_name, jdata['password'])
    click_element_by_xpath(driver, password_next_xpath)
    close_driver(driver)
	
	
test_login_gmail()	









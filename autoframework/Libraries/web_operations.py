from selenium import webdriver
from time import sleep

def open_chrome_browser(url):
    '''
    To open a chrome brower with given url
    '''
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        sleep(2)
        return driver
    except Exception as e:
        driver.save_screenshot(r"C:\Users\mubarak\Desktop\autoframework\Logs\browser_error.png")
        raise AssertionError('Not able to open browser due to :', e)

def click_element_by_xpath(d,xpath):
    try:
        sleep(2)
        e = d.find_element_by_xpath(xpath)
        e.click()
    except Exception as e:
        d.save_screenshot(r"C:\Users\mubarak\Desktop\autoframework\Logs\click_error.png")
        raise AssertionError('Not able to click due to :', e)

def enter_text_by_id(d,id, text):
    try:
        sleep(2)
        e = d.find_element_by_id(id)
        e.send_keys(text)
    except Exception as e:
        d.save_screenshot(r"C:\Users\mubarak\Desktop\autoframework\Logs\enter_text_error.png")
        raise AssertionError('Not able to enter text due to :', e)

def enter_text_by_name(d,name, text):
    sleep(2)
    try:
        e = d.find_element_by_name(name)
        e.send_keys(text)
    except Exception as e:
        d.save_screenshot(r"C:\Users\mubarak\Desktop\autoframework\Logs\enter_text_error.png")
        raise AssertionError('Not able to enter text due to :', e)


def close_driver(d):
    sleep(2)
    try:
        d.close()
    except Exception as e:
        d.save_screenshot(r"C:\Users\mubarak\Desktop\autoframework\Logs\close_driver.png")
        raise AssertionError('Not able to close browser due to :', e)
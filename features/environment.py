from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from base.commonmethods import CommonMethods
import os
import platform
import time


def before_all(context):
    url = 'https://172.172.172.172'
    driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'driver'))
    os_name = platform.system()

    if os_name == "Linux" or os_name == "Linux2":
        driver_path = driver_path + "/chromedriver_linux64/chromedriver"
    elif os_name == "Darwin":
        driver_path = driver_path + "/chromedriver_mac32/chromedriver"
    elif os_name == "Windows":
        driver_path = driver_path + "/chromedriver_win32/chromedriver"

    options = Options()
    context.driver = webdriver.Chrome(driver_path)
    context.driver.maximize_window()
    context.url = url
    context.driver.get(url)

    mCommonmethods = CommonMethods(context.driver)

    WebDriverWait(context.driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "signin")))
    mCommonmethods.send_keys("your-username", "username")
    context.driver.find_element_by_id("password").send_keys("your-password")
    context.driver.find_element_by_id('login-button').click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Dashboard"))
    time.sleep(3)

    try:
        context.driver.find_element_by_id('alert')
    except NoSuchElementException:
        pass
    else:
        raise AssertionError('An error occurred while loading Dashboard page')


def after_all(context):
    context.driver.quit()

def after_all_steps(context):
    time.sleep(0.5)

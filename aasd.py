from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
firefox_options = Options()
list_prices = []



print("1")
def browser_data():
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument('window-size=1920x1080')
    print("2")
    browser = webdriver.Firefox(executable_path='C:/Users/Johan/Webdrivers/geckodriver')#, options=firefox_options)
    print("3")
    start_URL = "https://www.plus500.se/"
    print("4")
    browser.get(start_URL)
    print("5")
    print(browser.title)
    search_click = browser.find_element_by_xpath('/html/body/header/section/div/div/div/div[2]/div/div[2]/button')
    search_click.click()
    search_bar = browser.find_element_by_xpath('//*[@id="searchInstruments"]')
    time.sleep(1)
    search_bar.send_keys("AMD")
    time.sleep(2)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(1)
    number_of_times = 0

    while True:
        now = datetime.now()
        price = browser.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div[1]/div[1]/p[1]/span[1]')
        current_time = now.strftime("%H:%M:%S")
        time_and_price = (current_time, price.text)
        print(time_and_price)
        number_of_times += 1
        browser.refresh()
        list_prices.extend(time_and_price)
        if number_of_times == 3:
            break
        time.sleep(2)

    print(list_prices)


browser_data()

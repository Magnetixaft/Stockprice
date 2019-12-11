from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Phantom_path = 'C:/Users/Johan/Webdrivers/phantomjs'
browser = webdriver.PhantomJS(executable_path=Phantom_path)

start_URL = "https://http://www.plus500.se/"
print("0")
browser = webdriver.PhantomJS(executable_path='C:/Users/Johan/Webdrivers/phantomjs')
print("3")
start_URL = "https://www.plus500.se/"
print("4")
browser.get(start_URL)
print("5")
print(browser.title)
time.sleep(1)
search_click = browser.find_element_by_xpath('/html/body/header/section/div/div/div/div[2]/div/div[2]/button')
time.sleep(2)
print("6")
search_click.click()
print("7")
time.sleep(1)
search_bar = browser.find_element_by_xpath('//*[@id="searchInstruments"]')
search_bar.clear()
search_bar.send_keys("AMD")
time.sleep(1)
search_bar.send_keys(Keys.RETURN)

price = browser.find_element_by_xpath('//*[@id="instrment-data"]/div/div[1]/div[1]/p[1]/span[1]')
print(price.text)
browser.quit()
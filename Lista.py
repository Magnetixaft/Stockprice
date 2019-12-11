from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


chromedriver = "C:/Users/Johan/Webdrivers/chromedriver"
browser = webdriver.Chrome(executable_path = chromedriver, chrome_options = options)
browser.get("https://markets.businessinsider.com/stocks")

print(browser.title)
search_click = browser.find_element_by_xpath('//*[@id="simple-menu-search"]/span')
search_click.click()
search_bar = browser.find_element_by_xpath('//*[@id="search-input"]')
time.sleep(1)
search_bar.clear()
time.sleep(1)
search_bar.send_keys("AMD")

search_bar.send_keys(Keys.RETURN)
price = browser.find_element_by_xpath('//*[@id="site"]/div/div[2]/div[3]/div/div[1]/div[1]/div[3]/div[1]/span')
print(price.text)
browser.quit()
from worldtradingdata import WorldTradingData
from selenium import webdriver
browser = webdriver.Chrome(executable_path='C:/Users/Johan/Webdrivers/chromedriver')

my_api_token = ("q2BYv8bIBj5gIwb95w4Mr6yPluepsDIDP2CrkeRaSP4A7d8oQ2mTfU6sGL1h")
wtd = WorldTradingData(my_api_token)
wtd.stock_search("AAPL")

browser.get('https://api.worldtradingdata.com/api/v1/history')
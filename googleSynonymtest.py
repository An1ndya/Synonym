from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd


#word = input("Write down a single word : ")
word = "run"
url = 'https://www.google.com/search?q=define+' + word

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content)

print(soup)
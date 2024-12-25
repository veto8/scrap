#!/usr/bin/env python
import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless=new") # for Chrome >= 109

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.tops.co.th/en/fruit-and-vegetables')

soup = BeautifulSoup(browser.page_source, "html.parser")

items = soup.find_all('div', {'class': 'mt-product-item'})
print(items)



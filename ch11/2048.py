#! python3
# 2048.py will go to the 2048 game website and play the automatically with
## up,right,left and down arrows given by selenium Keys module

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4, requests, time, random

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

randKey = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

for i in range(1, 100, 1):
	htmlElem.send_keys(random.choice(randKey))
	time.sleep(0.1)
	htmlElem.send_keys(random.choice(randKey))
	time.sleep(0.1)
	htmlElem.send_keys(random.choice(randKey))
	time.sleep(0.1)
	htmlElem.send_keys(random.choice(randKey))
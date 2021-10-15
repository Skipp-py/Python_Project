from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import random
import collector

collector.driver.get('https://www.airbnb.com/s/experiences/online')

category_button = collector.driver.find_element_by_xpath(
    "//span[@aria-label='Family friendly']")

try:
    time.sleep(2)
    category_button.click()
except:
    time.sleep(2)
    category_button.click()

time.sleep(4)
good_for_groups = collector.collect_href()

print(good_for_groups[:5])

collector.driver.close()

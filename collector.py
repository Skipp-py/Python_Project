from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import random

driver = webdriver.Chrome('/Users/skippy/Desktop/NYCDSA/chromedriver')

driver.get('https://www.airbnb.com/s/experiences/online')


group_button = driver.find_element_by_xpath(
    "//span[@aria-label='Great for groups']")

try:
    time.sleep(2)
    group_button.click()
except:
    time.sleep(2)
    group_button.click()

element = driver.find_element_by_xpath("//button[@class='_pmpl8qu']")


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    wait_time = random.randrange(2, 5)

    time.sleep(wait_time)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        time.sleep(wait_time)
        element.click()
    finally:
        # Wait to load page
        time.sleep(wait_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver.close()

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import random
import collector

# Launch driver and open site
collector.driver.get('https://www.airbnb.com/s/experiences/online')

time.sleep(2)

# Maximize the window after page loads
collector.driver.maximize_window()

category_buttons = collector.driver.find_elements_by_xpath(
    "//button[@class='_1n56hy1']")

next_button = collector.driver.find_element_by_xpath(
    "//button[@aria-label='Next' and @class='_137uqvg']")

d = {}

for i in range(15, 17):
    try:
        time.sleep(2)
        category_buttons[i].click()
    except:
        try:
            time.sleep(2)
            category_buttons[i].click()
        except:
            time.sleep(2)
            next_button.click()
            time.sleep(2)
            category_buttons[i].click()
    finally:
        time.sleep(2)
        lst = collector.collect_href()
        d[category_buttons[i].text] = lst[:5]
        collector.driver.execute_script("window.history.go(-1)")

# time.sleep(4)
# good_for_groups = collector.collect_href()

# print(good_for_groups[:5])

print(d.items())
collector.driver.close()

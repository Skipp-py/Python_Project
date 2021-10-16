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

final_dict = {'Experience_Name': [], 'Rating': [], 'Reviews': [], 'City': [], 'Country': [], 'Duration': [], 'Languages': [], 'Cost_Adult': [], 'Cost_Child': [], 'Cost_Infant': [],
              'Cost_Infant': [], 'Group_Start_Cost': [], 'Group_Limit': [], 'Group_Discount': [], 'Sold_Out': []}

for i in range(9, 10):
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
        for url in lst:
            time.sleep(2)
            d = collector.page_info(url)
            for k, v in d.items():
                if k in final_dict.keys():
                    final_dict[k] += v
            else:
                final_dict[k] = v
        collector.driver.execute_script("window.history.go(-2)")


print(final_dict.items())
collector.driver.close()

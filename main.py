from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import random
import collector
import pandas as pd

# Launch driver and open site
collector.driver.get('https://www.airbnb.com/s/experiences/online')

time.sleep(2)

# Maximize the window after page loads
collector.driver.maximize_window()

category_buttons = collector.driver.find_elements_by_xpath(
    "//button[@class='_1n56hy1']")

next_button = collector.driver.find_element_by_xpath(
    "//button[@aria-label='Next' and @class='_137uqvg']")

final_dict = {'Experience_Name': [], 'Rating': [], 'Reviews': [], 'City': [], 'Country': [], 'Duration': [], 'Languages': [
], 'Cost': [], 'Group_Limit': [], 'Group_Start_Cost': []}


unique_urls = []

for i in range(4, 5):
    try:
        time.sleep(1)
        category_buttons[i].click()
    except:
        try:
            time.sleep(1)
            category_buttons[i].click()
        except:
            time.sleep(2)
            next_button.click()
            time.sleep(2)
            category_buttons[i].click()
    finally:
        lst = collector.collect_href()
        for url in lst:
            if url in unique_urls:
                continue
            else:
                unique_urls.append(url)
        time.sleep(1)
        collector.driver.execute_script("window.history.go(-1)")

for url in unique_urls:
    d = collector.page_info(url)
    for k, v in d.items():
        if k in final_dict.keys():
            final_dict[k] += v
        else:
            final_dict[k] = v

print(final_dict.items())

print('Titles: ' + str(len(final_dict['Experience_Name'])))
print('Ratings: ' + str(len(final_dict['Rating'])))
print('Reviews: ' + str(len(final_dict['Reviews'])))
print('Cities: ' + str(len(final_dict['City'])))
print('Countries: ' + str(len(final_dict['Country'])))
print('Duration: ' + str(len(final_dict['Duration'])))
print('Lanuages: ' + str(len(final_dict['Languages'])))
print('Costs: ' + str(len(final_dict['Cost'])))
print('Group_Start_Cost: ' + str(len(final_dict['Group_Start_Cost'])))
print('Group_Limit: ' + str(len(final_dict['Group_Limit'])))

df = pd.DataFrame.from_dict(final_dict)

df.to_csv('project_baking.csv', index=False)

collector.driver.close()

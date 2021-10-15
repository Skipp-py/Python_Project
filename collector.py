from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import random

driver = webdriver.Chrome('/Users/skippy/Desktop/NYCDSA/chromedriver')


def collect_href():

    page_hrefs = []

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        try:
            load_button = driver.find_element_by_xpath(
                "//button[@class='_pmpl8qu']")
        except:
            continue
        finally:
            wait_time = random.randrange(2, 4)

            time.sleep(wait_time)

            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            try:
                time.sleep(wait_time)
                load_button.click()
            finally:
                # Wait to load page
                time.sleep(wait_time)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script(
                    "return document.body.scrollHeight")
                if new_height == last_height:
                    elems = driver.find_elements_by_xpath(
                        "//a[@class='_1jhvjuo']")
                    for ele in elems:
                        page_hrefs.append(ele.get_attribute('href'))
                    break
                last_height = new_height

    return page_hrefs

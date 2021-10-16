from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

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

            time.sleep(2)

            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            try:
                time.sleep(2)
                load_button.click()
            finally:
                # Wait to load page
                time.sleep(2)

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


def page_info(url):

    driver.get(url)

    d = {'Experience_Name': [], 'Rating': [], 'Reviews': [], 'City': [], 'Country': [], 'Duration': [], 'Languages': [
    ], 'Cost': [], 'Group_Limit': [], 'Group_Start_Cost': []}

    def pricing_split(lst):
        for x in lst:
            if 'Adult' in x[0] or 'Each' in x[0]:
                d['Cost'].append(x[1])
            elif 'Up to' in x[0]:
                d['Group_Limit'].append(re.sub('[^0-9]', '', x[0]))
                d['Group_Start_Cost'].append(x[1])

    time.sleep(5)
    try:
        d['Rating'].append(driver.find_element_by_xpath(
            "//span[@class='_1di55y9']").text)
    except:
        d['Rating'].append(None)

    try:
        location = driver.find_elements_by_xpath(
            "//span[@class='_11waoz2']")[0].text.split(',')
        if location[0] == 'Olympian and Paralympian collection':
            d['City'].append(None)
            d['Country'].append(None)
        else:
            d['City'].append(location[0])
            d['Country'].append(location[1].lstrip())
    except:
        d['City'].append(None)
        d['Country'].append(None)

    try:
        d['Experience_Name'].append(
            driver.find_element_by_xpath("//h1[@class='_14i3z6h']").text)
    except:
        d['Experience_Name'].append(None)

    try:
        duration = driver.find_element_by_xpath(
            "//div[@class='_13wkz77']").text.split('\n')
        duration = list(map(lambda x: re.sub(
            '[^A-Za-z0-9 ]+', '', x).lstrip(), duration))
        duration_language = [ele for ele in duration if ele]

        d['Duration'].append(re.sub('[^0-9]+', '', duration_language[0]))
        d['Languages'].append(duration_language[1])
    except:
        d['Duration'].append(None)
        d['Languages'].append(None)

    try:
        d['Reviews'].append(re.sub('[^0-9]', '', driver.find_elements_by_xpath(
            "//span[@class='l1dfad8f dir dir-ltr']")[0].text))
    except:
        d['Reviews'].append(None)

    try:
        prices_button = driver.find_element_by_xpath(
            "//button[@class='_1u40q3ee']")
        prices_button.click()
        time.sleep(2)
        prices_xpath = driver.find_elements_by_xpath(
            "//div[@class='_1iq4q55']")
        prices = [ele.text for ele in prices_xpath]
        price = list(map(lambda x: x.split('\n'), prices))
        customer = [x[0] for x in price]
        value = list(map(lambda x: re.sub('[^$0-9%]+', '', x[1]), price))
        pricing = list(zip(customer, value))
        pricing_split(pricing)
        time.sleep(1)
        if d['Group_Start_Cost'] == [] and d['Group_Limit'] == []:
            d['Group_Start_Cost'].append(None)
            d['Group_Limit'].append(None)

    except:
        d['Cost'].append(re.sub('[^$0-9%]+', '', driver.find_element_by_xpath(
            "//div[@class='_aryd7a']").text))
        d['Group_Start_Cost'].append(None)
        d['Group_Limit'].append(None)

    return d

import time

from selenium import webdriver
from datetime import datetime

from selenium.webdriver.common.by import By

chrome_path = "/home/amrutraj/PycharmProjects/Python/Day48/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
# cook = driver.find_element('id', 'cookie')
# time1 = datetime.now()
# while True:
#     cook.click()
#     if (time1-datetime.now()).seconds >= 5:
#         time1 = datetime.now()
#         mo = driver.find_element('id', 'money')
cookie = driver.find_element("id", "cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element('id', to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    # if time.time() > five_min:
    #     cookie_per_s = driver.find_element('id', "cps").text
    #     print(cookie_per_s)
    #     driver.quit()
    #     break
        


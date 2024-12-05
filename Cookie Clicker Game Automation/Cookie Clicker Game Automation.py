
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


URL = "https://orteil.dashnet.org/experiments/cookie/"

time_limit = time.time() + 60*5 # 5 minutes
five_second_delay = 5
timer = time.time()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Get upgrade attribute ids.
attributes = driver.find_elements(By.CSS_SELECTOR, "#store div")
all_attributes = [attribute.get_dom_attribute("id") for attribute in attributes]

while time.time() < time_limit:

    # Get cookie to click on.
    cookie_click = driver.find_element(By.ID, "cookie")
    cookie_click.click()

    if time.time() > timer + five_second_delay:

        score = driver.find_element(By.ID, "money").text
        if "," in score:
            score = score.replace(",", '')
        the_score = int(score)

        points = driver.find_elements(By.CSS_SELECTOR, "#store b")
        all_points = []

        for point in points:
            the_point = point.text
            if the_point != "":
                cost = int(the_point.split("-")[1].strip().replace(",", ""))
                all_points.append(cost)

        cookie_upgrade = {}
        for n in range(len(all_points)):
            cookie_upgrade[all_points[n]] = all_attributes[n]

        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if the_score > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

        timer = time.time()


cookies_per_second = driver.find_element(By.ID, "cps").text

print(cookies_per_second)






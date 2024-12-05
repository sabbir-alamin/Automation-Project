from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Sabbir")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Al-Amin")

email = driver.find_element(By.CLASS_NAME, "bottom")
email.send_keys("alamin170@gmail.com")

button_click = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button_click.click()

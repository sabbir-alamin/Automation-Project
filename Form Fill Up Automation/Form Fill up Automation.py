from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "http://secure-retreat-92358.herokuapp.com/"

# Prevent the browser from closing automatically after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the specified web page in the browser
driver.get(URL)

# Locate the "First Name" input field using its 'name' attribute and input a value
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Sabbir")

# Locate the "Last Name" input field using its 'name' attribute and input a value
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Al-Amin")

# Locate the "Email" input field using its 'class' attribute and input a value
email = driver.find_element(By.CLASS_NAME, "bottom")
email.send_keys("alamin170@gmail.com")

# Locate the "Submit" button using its CSS selector and simulate a click action
button_click = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button_click.click()


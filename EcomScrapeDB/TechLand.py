from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options to keep the browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(chrome_options)

# Target URL for scraping
URL = "https://www.techlandbd.com/shop-laptop-computer/brand-laptops/apple-macbook?limit=75"

# Open the specified URL in the browser
driver.get(URL)

""" PRICE """

# Locate all elements containing laptop prices by their class name
laptop_price = driver.find_elements(By.CLASS_NAME, 'price')

# Extract the text from each located price element and store in a list
laptop_price_list = [prices.text for prices in laptop_price]

# Intermediate lists for processing the prices
p = []  # A temporary list to store split prices
new_list = []  # A cleaned list of extracted prices

# Split price text by "৳" and organize into a list for further processing
for items in laptop_price_list:
    val = items.split("৳")
    p.append(val)

# Process the price list to clean up unwanted values and isolate numeric parts
for values in range(len(p)):
    if len(p[values]) == 1:  # Handle entries with a single value
        pop1 = p[values].pop(0)
    elif len(p[values]) == 2:  # Handle entries with two values
        pop2 = p[values].pop(1)
    elif len(p[values]) == 3:  # Handle entries with three values
        pop3 = p[values].pop(1)
        pop4 = p[values].remove('')  # Remove any empty strings

# Further clean up and extract the first numeric value from each entry
for k in range(len(p)):
    if p[k]:
        new_list.append(p[k][0])

# Convert the cleaned price strings to floating-point numbers
tech_laptop_prices = []
for prices in new_list:
    price = float(prices.replace(",", ""))  # Remove commas before conversion
    tech_laptop_prices.append(price)

""" tech_laptop_prices contains the final list of laptop prices """

""" MODEL """

# Locate all elements containing laptop names by their class name
laptop_name = driver.find_elements(By.CLASS_NAME, "name")

# Extract the text from each located name element and store in a list
tech_laptop_name_list = [names.text for names in laptop_name]

""" tech_laptop_name_list contains the final list of laptop names """

""" MODEL LINK """

# Locate all anchor elements within elements having the "name" class
link = driver.find_elements(By.CSS_SELECTOR, ".name a")

# Extract the href attribute (link) from each anchor element
tech_link_list = []
for links in link:
    web_link = links.get_attribute("href")
    if web_link:  # Ensure the link is not empty
        tech_link_list.append(web_link)

""" tech_link_list contains the final list of links for each laptop model """

from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options to prevent the browser from closing after execution
chromo = webdriver.ChromeOptions()
chromo.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(chromo)

# URL of the site to scrape
URL = "https://www.startech.com.bd/apple-macbook?limit=75"

# Open the specified URL in the browser
driver.get(URL)

""" MODEL """

# Locate all elements containing product model names using their class name
product_model = driver.find_elements(By.CLASS_NAME, "p-item-name")

# Extract the text content of each model element and store it in a list
product_model_list = [models.text for models in product_model]

# product_model_list contains the names of all products
""" >>> product_model_list <<< """

""" PRICE """

# Locate all elements containing product prices using their class name
product_price = driver.find_elements(By.CLASS_NAME, "p-item-price")

# Extract the text content of each price element and store it in a list
product_price_list = [models.text for models in product_price]

# Temporary lists to assist with cleaning and processing prices
r = []  # List to hold split values
new_list = []  # Cleaned list of price values

# Split the price text by "৳" to isolate numeric values
for items in product_price_list:
    val = items.split("৳")
    r.append(val)

# Process the split list to remove unwanted entries and clean the data
for values in range(len(r)):
    if len(r[values]) == 1:  # Handle entries with one part
        pop1 = r[values].pop(0)
    elif len(r[values]) == 2:  # Handle entries with two parts
        pop2 = r[values].pop(1)
    elif len(r[values]) == 3:  # Handle entries with three parts
        pop3 = r[values].pop(1)
        pop4 = r[values].remove('')  # Remove empty strings

# Extract the numeric part of the price and append to the new list
for k in range(len(r)):
    if r[k]:  # Ensure the entry is not empty
        new_list.append(r[k][0])

# Convert the cleaned price strings to floating-point numbers
all_prices = []
for prices in new_list:
    price = float(prices.replace(",", ""))  # Remove commas and convert to float
    all_prices.append(price)

# all_prices contains the numeric prices of all products
""" >>> all_prices <<< """

""" URL """

# Locate anchor elements within the product item container to extract product URLs
link = driver.find_elements(By.CSS_SELECTOR, '.p-item a')

# Extract the href attribute (URL) from each anchor element
link_list = []
for links in link:
    web_url = links.get_attribute("href")
    if web_url:  # Ensure the URL is valid
        link_list.append(web_url)

# link_list contains the URLs of all product pages
""" >>> link_list <<< """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configure Chrome options to keep the browser open after script execution
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_option)

# URL of the site to scrape
site_url = "https://www.ryans.com/category/all-laptop-apple?limit=100&sort=D&osp=1&st=0"

# Open the target site in the browser
driver.get(site_url)

""" PRICE """

# Locate all elements containing price details by their class name
product_price_details = driver.find_elements(By.CLASS_NAME, "text-decoration-none")

# Extract the text from each located price element and store it in a list
product_price_list = [val.text for val in product_price_details]

# Clean up the price list by removing text after "...\n" and ignoring empty strings
cleaned_list = [
    item.split("...\n")[0]  # Retain only the portion before '...\n'
    for item in product_price_list
    if item.strip()  # Remove any blank strings
]

# Initialize a list to store cleaned numeric price values
ryans_product_price_list = []

# Process the cleaned list to extract valid price numbers
for item in cleaned_list:
    if "Tk" in item:  # Ensure the item contains the currency marker
        # Remove currency symbols, estimated text, and commas, then convert to float
        cleaned_price = item.replace("Tk", '').replace("(Estimated)", '').replace(",", '').strip()
        ryans_product_price_list.append(float(cleaned_price))

""" MODEL """

# Locate elements containing product names or model numbers
model_no2 = driver.find_elements(By.CSS_SELECTOR, ".h-100 a")

# Extract the text content of each located element
model_text2 = [models.text for models in model_no2]

# Stepwise filtering to clean up and isolate model names
filter1 = [products.split("...\n")[0] for products in model_text2 if products.strip()]  # Remove text after '...\n'
filter2 = [goods.split("Tk")[0] for goods in filter1 if goods]  # Remove text containing 'Tk'
filter3 = [elements for elements in filter2 if elements]  # Retain non-empty entries

""" URL """

# Locate anchor elements with text containing 'Tk' (price links)
links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Tk')]")

# Extract the href attribute (URL) from each anchor element
url_list = []
for link in links:
    url = link.get_attribute("href")
    if url:  # Ensure the URL is valid
        url_list.append(url)

""" 2nd Page Scraping """

# Locate and interact with the pagination button to navigate to the next page
button = driver.find_element(By.CSS_SELECTOR, ".page-item a")
button.send_keys(Keys.ENTER)

""" PRICE 2 """

# Locate elements containing price details on the second page
product_price_details2 = driver.find_elements(By.CLASS_NAME, "text-decoration-none")

# Extract the text from each located price element
product_price_list2 = [val.text for val in product_price_details2]

# Clean up the price list similarly to the first page
cleaned_list2 = [
    item.split("...\n")[0]  # Retain only the portion before '...\n'
    for item in product_price_list2
    if item.strip()  # Remove any blank strings
]

# Extract and clean price values from the second page
valid_price_list2 = []
for item in cleaned_list2:
    if "Tk" in item:  # Ensure the item contains the currency marker
        # Remove currency symbols, estimated text, and commas, then convert to float
        cleaned_price2 = item.replace("Tk", '').replace("(Estimated)", '').replace(",", '').strip()
        valid_price_list2.append(float(cleaned_price2))

""" MODEL 2 """

# Locate elements containing product names or model numbers on the second page
model_no2 = driver.find_elements(By.CSS_SELECTOR, ".h-100 a")

# Extract and clean up model names from the second page
model_text2 = [models.text for models in model_no2]
filter4 = [products.split("...\n")[0] for products in model_text2 if products.strip()]  # Remove text after '...\n'
filter5 = [goods.split("Tk")[0] for goods in filter4 if goods]  # Remove text containing 'Tk'
filter6 = [elements for elements in filter5 if elements]  # Retain non-empty entries

""" URL 2 """

# Locate anchor elements with text containing 'Tk' on the second page
links2 = driver.find_elements(By.XPATH, "//a[contains(text(), 'Tk')]")

# Extract the href attribute (URL) from each anchor element
url_list2 = []
for link2 in links2:
    url2 = link2.get_attribute("href")
    if url2:  # Ensure the URL is valid
        url_list2.append(url2)

# Combine data from both pages
ryans_product_price = ryans_product_price_list + valid_price_list2  # Combined price list
ryans_product_models = filter3 + filter6  # Combined model list
ryans_product_url = url_list + url_list2  # Combined URL list

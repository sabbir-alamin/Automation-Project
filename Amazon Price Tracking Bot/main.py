import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# Email credentials for sending alerts
MAIL = "YOUR MAIL"
PASSWORD = "YOUR PASSWORD"

# URL of the Amazon product to monitor
URL = "https://www.amazon.com/dp/B075CWJ3T8?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# HTTP headers to mimic a legitimate browser request
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
ACCEPT_ENCODING = "gzip, deflate, br, zstd"
UPGRADE_INSECURE_REQUESTS = "1"
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

# Headers dictionary for the GET request
header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
    "Accept-Encoding": ACCEPT_ENCODING,
    "Upgrade-Insecure-Requests": UPGRADE_INSECURE_REQUESTS,
    "Accept": ACCEPT,
}

# Send an HTTP GET request to the product page
response = requests.get(url=URL, headers=header)

# Parse the HTML content using BeautifulSoup with the lxml parser
soup = BeautifulSoup(response.content, "lxml")

# Extract the product price from the HTML using its class name
price = soup.find(class_="a-offscreen").get_text()

# Transforming the price into a numeric value
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

# Check if the price is below a certain threshold and send mail
if price_as_float < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs="sabbiralamin707@gmail.com",
            msg=(
                f"Subject:Amazon Price Alert!! \n\n"
                f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, "
                f"Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, "
                f"Stainless Steel, 8 Quart is now {price_as_float}$"
            ).encode("utf-8")
        )

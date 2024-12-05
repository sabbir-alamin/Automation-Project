import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MAIL = "rebillion.bir@gmail.com"
PASSWORD = "ucon gdct xtbg muwx"

URL = "https://www.amazon.com/dp/B075CWJ3T8?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
ACCEPT_ENCODING = "gzip, deflate, br, zstd"
UPGRADE_INSECURE_REQUESTS = "1"
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
X_HTTPS = "on"

header = {

    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
    "Accept-Encoding": ACCEPT_ENCODING,
    "Upgrade-Insecure-Requests": UPGRADE_INSECURE_REQUESTS,
    "Accept": ACCEPT,

}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MAIL,
                            to_addrs="sabbiralamin707@gmail.com",
                            msg=f"Subject:Amazon Price Alter!! \n\nInstant Pot Duo Plus 9-in-1 Electric Pressure "
                                f"Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, "
                                f"Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, "
                                f"8 Quart is now {price_as_float}$".encode("utf-8")
                            )

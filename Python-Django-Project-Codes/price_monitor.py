import requests
from bs4 import BeautifulSoup
import smtplib
import json
import os

# Configuration
ITEMS = [
    {
        'name': 'Item 1',
        'url': 'https://competitor-site.com/product1',
        'selector': '.price'  # CSS selector for price element
    },
    # Add more items here
]

PRICE_DATA_FILE = 'price_data.json'
EMAIL_SENDER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
EMAIL_RECEIVER = 'your_email@example.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def load_previous_prices():
    if os.path.exists(PRICE_DATA_FILE):
        with open(PRICE_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_current_prices(prices):
    with open(PRICE_DATA_FILE, 'w') as f:
        json.dump(prices, f)

def get_price(url, selector):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one(selector)
        if price_element:
            # Extract numeric value from price text
            price_text = price_element.get_text().strip()
            price = float(''.join(filter(str.isdigit, price_text)))
            return price
        else:
            print(f"Price element not found for {url}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def send_email(subject, body):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    previous_prices = load_previous_prices()
    current_prices = {}
    alerts = []

    for item in ITEMS:
        name = item['name']
        url = item['url']
        selector = item['selector']
        current_price = get_price(url, selector)
        if current_price is not None:
            current_prices[name] = current_price
            prev_price = previous_prices.get(name)
            if prev_price and prev_price != current_price:
                alerts.append(f"{name} price changed from {prev_price} to {current_price}")
            elif not prev_price:
                alerts.append(f"{name} current price is {current_price}")

    # Save current prices for next comparison
    save_current_prices(current_prices)

    # Send alert if there are changes
    if alerts:
        send_email("Price Change Alert", "\n".join(alerts))
    else:
        print("No price changes detected.")

if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup
import smtplib
import json
import os

# Configuration
ITEMS = [
    {
        'name': 'Item 1',
        'url': 'https://competitor-site.com/product1',
        'selector': '.price'  # CSS selector for price element
    },
    # Add more items here
]

PRICE_DATA_FILE = 'price_data.json'
EMAIL_SENDER = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
EMAIL_RECEIVER = 'your_email@example.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def load_previous_prices():
    if os.path.exists(PRICE_DATA_FILE):
        with open(PRICE_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_current_prices(prices):
    with open(PRICE_DATA_FILE, 'w') as f:
        json.dump(prices, f)

def get_price(url, selector):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.select_one(selector)
        if price_element:
            # Extract numeric value from price text
            price_text = price_element.get_text().strip()
            price = float(''.join(filter(str.isdigit, price_text)))
            return price
        else:
            print(f"Price element not found for {url}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def send_email(subject, body):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    previous_prices = load_previous_prices()
    current_prices = {}
    alerts = []

    for item in ITEMS:
        name = item['name']
        url = item['url']
        selector = item['selector']
        current_price = get_price(url, selector)
        if current_price is not None:
            current_prices[name] = current_price
            prev_price = previous_prices.get(name)
            if prev_price and prev_price != current_price:
                alerts.append(f"{name} price changed from {prev_price} to {current_price}")
            elif not prev_price:
                alerts.append(f"{name} current price is {current_price}")

    # Save current prices for next comparison
    save_current_prices(current_prices)

    # Send alert if there are changes
    if alerts:
        send_email("Price Change Alert", "\n".join(alerts))
    else:
        print("No price changes detected.")

if __name__ == "__main__":
    main()
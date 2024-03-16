import requests
from bs4 import BeautifulSoup

def get_amazon_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Based on the provided structure, finding the price within a specific class
        price = soup.find("span", {"class": "a-size-base a-color-price"})
        if price:
            return price.text.strip()
        else:
            return "Price not found"
    else:
        return "Failed to fetch page"

def get_ebay_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Based on the provided structure, finding the price within a specific class
        price = soup.find("div", {"class": "x-price-primary"}).find("span", {"class": "ux-textspans"})
        if price:
            return price.text.strip()
        else:
            return "Price not found"
    else:
        return "Failed to fetch page"

# URLs provided for each book
amazon_url = "https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844"
ebay_url = "https://www.ebay.com/p/73175956"

# Print the prices
print("Amazon Price:", get_amazon_price(amazon_url))
print("eBay Price:", get_ebay_price(ebay_url))

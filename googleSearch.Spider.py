import requests
from bs4 import BeautifulSoup

def get_barnes_noble_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting price
        price_element = soup.select_one('.bned-price-container .price')
        price = price_element.get_text(strip=True) if price_element else "Price not found"
        
        # Extracting full name
        name_element = soup.select_one('.product-details .name')
        name = name_element.get_text(strip=True) if name_element else "Name not found"
        
        return price, name, url
    except requests.RequestException as e:
        print(f"Error fetching Barnes & Noble details: {e}")
        return "Price not found", "Name not found", url

def get_ebay_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting name
        name_element = soup.select_one('.x-item-title__mainTitle')
        name = name_element.get_text(strip=True) if name_element else "Name not found"
        
        # Extracting format
        format_element = soup.select_one('.x-item-title__mainTitle .ux-textspans')
        format_name = format_element.get_text(strip=True) if format_element else "Format not found"
        
        # Extracting price
        price_element = soup.select_one('.x-price-primary .ux-textspans')
        price = price_element.get_text(strip=True) if price_element else "Price not found"
        
        return name, format_name, price, url
    except requests.RequestException as e:
        print(f"Error fetching eBay details: {e}")
        return "Name not found", "Format not found", "Price not found", url

# Example URLs
barnes_noble_url = "https://charlotte.bncollege.com/Categories/Trade-Books/Non-Fiction/Personal-Growth/Creativity/Burn-After-Writing/p/563821961"
ebay_url = "https://www.ebay.com/p/205709160"

# Get details from Amazon, Barnes & Noble, and eBay
barnes_noble_price, barnes_noble_name, barnes_noble_url = get_barnes_noble_details(barnes_noble_url)
ebay_name, ebay_format, ebay_price, ebay_url = get_ebay_details(ebay_url)

# Print the results
print("Barnes & Noble Details:")
print("Name:", barnes_noble_name)
print("Price:", barnes_noble_price)
print("URL:", barnes_noble_url)
print()

print("eBay Details:")
print("Name:", ebay_name)
print("Format:", ebay_format)
print("Price:", ebay_price)
print("URL:", ebay_url)
print()

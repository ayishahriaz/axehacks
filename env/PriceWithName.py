import requests
from bs4 import BeautifulSoup

def get_charlotte_book_details(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.select_one("div.product-details.page-title h1.name").text.strip()
        price = soup.select_one("div.bned-price-container-inner p.price").text.strip()
        return name, price
    else:
        return "Failed to fetch page", "Failed to fetch page"

def get_ebay_book_details(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.select_one("h1.x-item-title__mainTitle span").text.strip()
        price = soup.select_one("#mainContent > main > section.col-right > div.vim.x-price-section > div.vim.x-bin-price > div.x-bin-price__content > div.x-price-primary > span").text.strip()
        return name, price
    else:
        return "Failed to fetch page", "Failed to fetch page"

# URLs
charlotte_url = "https://charlotte.bncollege.com/Categories/Trade-Books/Non-Fiction/Personal-Growth/Creativity/Burn-After-Writing/p/563821961"
ebay_url = "https://www.ebay.com/p/205709160"

# Fetch and print book details
charlotte_name, charlotte_price = get_charlotte_book_details(charlotte_url)
print(f"Charlotte Barnes & Noble - Book Name: {charlotte_name}, Price: {charlotte_price}")

ebay_name, ebay_price = get_ebay_book_details(ebay_url)
print(f"eBay - Book Name: {ebay_name}, Price: {ebay_price}")

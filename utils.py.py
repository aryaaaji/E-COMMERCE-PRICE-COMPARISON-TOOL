# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

def ebay(name):
    try:
        name1 = name.replace(" ", "+")
        ebay_url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0'
        res = requests.get(ebay_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        length = soup.select('.s-item__price')
        ebay_page_length = len(length)

        for i in range(ebay_page_length):
            info = soup.select('.SECONDARY_INFO')[i].getText().strip().upper()

            if info == 'BRAND NEW':
                ebay_name = soup.select('.s-item__title')[i].getText().strip().upper()
                name = name.upper()

                if name in ebay_name[:25]:
                    ebay_price = soup.select('.s-item__price')[i].getText().strip()
                    ebay_name = soup.select('.s-item__title')[i].getText().strip()
                    ebay_price_inr = convert(ebay_price, is_usd=True)
                    ebay_price_original = convert(ebay_price, is_usd=True, return_original=True)
                    return f"{ebay_name}\nPrice: ₹{ebay_price_inr} (Original Price: {ebay_price_original})"
                else:
                    continue

        return 'Product Not Found on eBay'

    except Exception as e:
        return f'Error in eBay search: {e}'

def search_amazon(name):
    try:
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(amazon_url, headers=headers)
        print("\nSearching on Amazon...")
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = len(amazon_page)

        for i in range(amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()

            if name in amazon_name:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip()
                amazon_price_inr = convert(amazon_price)
                return f"{amazon_name}\nPrice: ₹{amazon_price_inr}"
                
        return 'Product Not Found on Amazon'

    except Exception as e:
        return f'Error in Amazon search: {e}'

def convert(price, is_usd=False, return_original=False):
    price = price.replace(" ", '').replace("INR", '').replace(",", '').replace("₹", '').replace('$', '').split('(')[0]

    if is_usd:
        # Check if the price is in a range format, e.g., '254.95to304.95'
        if 'to' in price:
            price_range = price.split('to')
            price_in_inr = (float(price_range[0]) + float(price_range[1])) / 2
            price_in_usd = price_in_inr / 83.27
            if return_original:
                return f"{price_range[0]} to {price_range[1]} USD"
            else:
                return int(price_in_inr)
        else:
            # Convert from dollars to Indian Rupees (1 USD = 83.27 INR)
            price_in_usd = float(price.strip().replace('USD', ''))
            price_in_inr = price_in_usd * 83.27
            if return_original:
                return f"{price} USD"
            else:
                return int(price_in_inr)
    else:
        price_in_inr = float(price)
        if return_original:
            return f"{price} INR"
        else:
            return int(price_in_inr)

def main():
    name = input("Product Name:\n")
    ebay_result = ebay(name)
    amazon_result = search_amazon(name)

    if 'Not Found' in ebay_result and 'Not Found' in amazon_result:
        print("Product not found on eBay and Amazon.")
    else:
        if 'Not Found' not in ebay_result:
            print("\nEBay Result:")
            print(ebay_result)
        else:
            print("\nEBay Result:")
            print("Product Not Found on eBay")

        if 'Not Found' not in amazon_result:
            print("\nAmazon Result:")
            print(amazon_result)
        else:
            print("\nAmazon Result:")
            print("Product Not Found on Amazon")

        print("\nComparison:")
        if 'Not Found' not in ebay_result and 'Not Found' not in amazon_result:
            ebay_price_inr = convert(ebay_result.split("Price: ₹")[1], is_usd=True)
            amazon_price_inr = convert(amazon_result.split("Price: ₹")[1])
            
            print(f"eBay Price: ₹{ebay_price_inr} (Original Price: {convert(ebay_result.split('Original Price: ')[1], is_usd=True, return_original=True)})")
            print(f"Amazon Price: ₹{amazon_price_inr} (Original Price: {convert(amazon_result.split('Original Price: ')[1], return_original=True)})")

            # Compare prices and print the result
            if ebay_price_inr < amazon_price_inr:
                print("eBay has a lower price.")
            elif ebay_price_inr > amazon_price_inr:
                print("Amazon has a lower price.")
            else:
                print("Prices on eBay and Amazon are the same.")

if __name__ == "__main__":
    main()

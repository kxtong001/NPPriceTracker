import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    #get product name
    name = soup.find(id="productTitle").getText()
    name = name.strip()
    
    #get product price - need filtering
    #notes: amz changes class name for prices quite frequently - need to change class name from time to time
    #get only 1 value, as duplicate values are produced
    prices = soup.find('span', class_= 'a-offscreen').getText()
    if prices != None:
        pricedata =  prices.split('$')
        price1 = pricedata[1]
        price = float(price1)
    else:
        prices = soup.find('span', class_= 'apexPriceToPay').getText()
        pricedata =  prices.split('$')
        price1 = pricedata[1]
        price = float(price1)
    #print(prices)


    #get product image
    imageurl = soup.find('img',{'alt':name})['src']
    #some pages do not load the correct image

    return name, price ,imageurl
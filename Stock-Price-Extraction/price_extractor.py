from bs4 import BeautifulSoup
import requests

def parsePrice():
    req = requests.get('https://finance.yahoo.com/quote/NQ%3DF?p=NQ%3DF')
    soup = BeautifulSoup(req.text, 'lxml')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text

print("NASDAQ Stock Price")
while True:
    print('th current price: '+str(parsePrice())) 
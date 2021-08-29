import requests
from bs4 import BeautifulSoup
import smtplib
import os

url = "https://www.amazon.in/dp/B08L5VZKWT" #product url you want to track
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
price_value = 127900                #budget value
email_address = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')
receive_email = os.environ.get('EMAIL_USER')

def trackPrice():
    price = float(getPrice())
    if price > price_value:
        diff = int(price - price_value)
        print(f"Still Rs{diff} too expensive!")
    else:
        print("Cheaper! Notifying...")
        sendEmail()

def getPrice():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title =soup.find(id="productTitle").get_text().strip()
    price =soup.find(id="priceblock_dealprice").get_text().strip().replace(',','')[1:]
    print(title)
    print(price)
    return price


def sendEmail():
    subject = "Amazon Price has Dropped!"
    mailtext = "Subject: "+subject+"\n\n"+url
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(email_address, password)
    server.sendmail(email_address, receive_email, mailtext)

if __name__ == '__main__':
    trackPrice()
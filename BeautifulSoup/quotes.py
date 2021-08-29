#Importing libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#page url and fetching the page
page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(page)

#getting the html data from the page
page_html = uClient.read()
uClient.close()

#parsing the html data
page_soup = soup(page_html, 'html.parser')
quotes = page_soup.findAll('div', {'class':'quotes'})

#getting the quotes
for quote in quotes:
    f_quote = quote.findAll('p', {'class':'aquote'})
    aquote = f_quote[0].text.strip()

    f_author = quote.findAll('p', {'class':'author'})
    author = f_author[0].text.strip()

    print('Quote : ',aquote)
    print('Author : ',author)
    print()


from cgitb import text
from email import header
from queue import Empty
from bs4 import BeautifulSoup
import requests




url = 'https://www.amazon.com/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0", 
    "X-Amzn-Trace-Id": "Root=1-61ea1f64-406799af58ffd3944aa20a36"}

html_text = requests.get(url,headers = headers).text

soup = BeautifulSoup(html_text, 'lxml')

def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)


###Extract the collection
url = 'https://www.amazon.com/s?k=gaming+mouse&crid=31HXHGEPP7U9C&sprefix=gaming+mous%2Caps%2C157&ref=nb_sb_noss_2'
html_text = requests.get(url,headers = headers)
soup = BeautifulSoup(html_text.content, 'html.parser')

items = soup.find_all('div','sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20')
slashed_price = soup.find_all('a', 'a-size-base a-link-normal s-link-style a-text-normal')
slashed_price2 = soup.find_all('span', {'data-a-strike': 'true'})
slashed_price3 = slashed_price2[0].find('span', {'class': 'a-offscreen'})


def getitems(soup):
    return
for item in items:
    prices = item.find('a', 'a-size-base a-link-normal s-link-style a-text-normal')
    try:
        price = prices.find('span', {'data-a-strike': 'true'})
        price_slash = prices.find('span', {'class': 'a-offscreen'})
        print('')
        print(price_slash.text.strip())
        print(price.text.strip())
        print('')
    except:
        print("NOT MARKED DOWN OR ON SALE") 
        
    finally:
        print("The 'try except' is finished") 
4
def getNextPage(soup):
    page = soup.find('ul', {'class': 'a-pagination'})
    if not page.find('li',{'class':'a-disabled a-last'}):
        url = 

def getdata(url):
    html= requests.get(url)
    soup= BeautifulSoup(html.text, headers)
    return(soup)

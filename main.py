from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0", 
    "X-Amzn-Trace-Id": "Root=1-61ea1f64-406799af58ffd3944aa20a36"}
html_text = requests.get(url,headers = headers).text
soup = BeautifulSoup(html_text, 'lxml')

def get_searched_item(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)


def get_soup(url):
    html= requests.get(url)
    soup= BeautifulSoup(html.text, headers)
    return(soup)

def get_item_list(soup):
    items = soup.find_all('div',{'class':'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20'})
    print(items[0])

def get_next_page(soup):
    page = soup.find('ul', {'class': 'a-pagination'})
    if not page.find('li',{'class':'a-disabled a-last'}):
        url = 'https://www.amazon.com/' + str (page.find('li',{'class','a-last'}).find('a')['href'])
        return url
    else:
        return

def get_marked_down_items(soup):
    items = soup.find_all('div','sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20')
    for item in items:
        prices = item.find('a', 'a-size-base a-link-normal s-link-style a-text-normal')
        try:
            price = prices.find('span', {'data-a-strike': 'true'})
            price_slash = prices.find('span', {'class': 'a-offscreen'})
            print('')
            print('Sale Price'+price_slash.text.strip())
            print('Original Price'+price.text.strip())

        except:
            print('this shit aint on sale')
            
        finally:
            print('done')

def get_discounted_items(soup):
    items = soup.find_all('span', {'class': 's-coupon-unclipped'})
    print(items)
    for item in items:
        
        coupon_amount = item.find('span',{'class':'a-size-base s-highlighted-text-padding aok-inline-block s-coupon-highlight-color'})
        print(coupon_amount.text)



url = 'https://www.amazon.com/s?k=gaming+mouse&crid=31HXHGEPP7U9C&sprefix=gaming+mous%2Caps%2C157&ref=nb_sb_noss_2'
html_text = requests.get(url,headers = headers)
soup = BeautifulSoup(html_text.content, 'html.parser')



def searched_item_check(soup, searched_item):
    items = soup.find_all('div','sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20')
    for item in items:
        item_title = item.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
        if searched_item.lower() in item_title.lower():
            print(item_title)
            print('this is a ' + searched_item)


items = soup.find_all('div',{'class':'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20'})
for item in items:
    item_title = item.find('span',{'class','a-size-medium a-color-base a-text-normal'})
    print(item_title.text)
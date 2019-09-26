import requests  # makes a call to a webpage
from bs4 import BeautifulSoup  # to parse and pull out individual items

url = 'https://www.amazon.com/Introducing-Echo-Show-Compact-Charcoal/dp/B07HZLHPKP/ref=sr_1_7?crid=' \
      '3EFN1G7P343T6&keywords=alexa&qid=1569520848&s=amazon-devices&sprefix=ale%2Caps%2C154&sr=1-7'

# creating a header with information from our browser. google search 'my user agent'. make sure it's a dictionary
headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
page = requests.get(url, headers=headers)  # the call to the webpage
soup = BeautifulSoup(page.content, 'html.parser')  # saves all webpage data
#print(soup.prettify())  # just to see what it prints


def check_price():
    price = soup.find(id='priceblock_ourprice').get_text()
    # print(price) >> $89.99
    # print(type(price))  >> class 'str'

    # convert the string into a float and remove the $. cannot compare str to str
    float_price = float(price[1:])
    print(float_price)  # >> 89.99
    print(type(float_price))  # >> class 'float'

    #if float_price < 50:
        #send_email()


check_price()

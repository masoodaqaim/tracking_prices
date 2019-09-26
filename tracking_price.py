import requests  # makes a call to a webpage
from bs4 import BeautifulSoup  # to parse and pull out individual items
import smtplib  # email protocols

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

    if float_price > 50.0:
        send_email()


# a function to set up a connection with this script to my gmail account
def send_email():
    server = smtplib.SMTP('stmp.gmail.com', 587)  # the 587 is the connection number
    server.ehlo()  # sets up the connection ???????
    server.starttls()  # encrypts the connection
    server.ehlo()

    server.login('masoodaqaimads@gmail.com', 'vknsxrhmvbibmchx')

    subject = 'Price of amazon product has decreased'
    body = 'Check amazon link for new price, https://www.amazon.com/dp/B07HZLHPKP?ref=ods_ucc_aucc_ch_rc_nd_ucc'

    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'masoodaqaimads@gmail.com',  # from
        'masoodaqaimads@gmail.com',  # to
        message  # message
    )
    print('email sent')  # just to check if an email has been sent. will only work if price is low

    server.quit()  # stopping the connection


check_price()

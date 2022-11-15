from twilio.rest import Client
import keys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.tradingview.com/markets/cryptocurrencies/prices-all/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

		
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

tablecells = soup.findAll('tr')



for row in tablecells[1:6]:
    td = row.findAll('td')
    name = td[0].text
    #no symbol on this webpage
    currentprice = (td[3].text)
    percent_change = (td[7].text.replace('%',""))
    corresp_price = float(currentprice)/(1+(float(percent_change)/100))

    
    print(name)
    print(f"Current price: $", currentprice)
    print(f"% change: ", percent_change,'%')
    print(f"The price before the % change: $", corresp_price)
    print()
    print()


client = Client(keys.accountSID, keys.authToken)
TwilioNumber = '+1 360 800 4311'
Mycellnum = '+12547442990'

for row in tablecells[1:2]:
    if float(currentprice) < 40000:
        textmsg = client.messages.create(to=Mycellnum, from_=TwilioNumber, body='Bitcoin has fallen below $40,000')
for row in tablecells[2:3]:
    if float(currentprice) < 3000:
        textmsg = client.messages.create(to=Mycellnum, from_=TwilioNumber, body='Ethereum has fallen below $3,000')


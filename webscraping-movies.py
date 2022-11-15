
from urllib.request import urlopen
from bs4 import BeautifulSoup






#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

tablerows = soup.findAll('tr')

for row in tablerows[1:6]:
    td = row.findAll('td')
    rank = td[0].text
    release=td[1].text
    total_gross = float(td[5].text.replace(",","").replace('$',""))
    distr = td[6].text
    theaters = int(td[6].text.replace(",",""))
    Avg_Revenue = round(total_gross/theaters,2)

    print('Rank: ', rank)
    print(f"Release: ", release)
    print(f"Total Gross: ", total_gross)
    print('Distributor: ', distr)
    print('Average revenue per theater: ', Avg_Revenue)
    print()
    print()
    





##
##
##
##


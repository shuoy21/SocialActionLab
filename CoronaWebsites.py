import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

url = "https://www.dallascounty.org/about-us/cities/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

city_urls = soup.find('div',{'id':'dc-listview'})


a_city = city_urls.find_all('a', href = True)
a_city_url = []
for i in a_city:
    a_city_url.append(i['href'])

temp = Request(a_city_url[0], headers={'User-Agent': 'Mozilla/5.0'})
temp_page = urlopen(temp).read()
temp_soup = BeautifulSoup(temp_page, 'html.parser')

find_coronavirus = temp_soup.find("coronavirus")




def find_coronawebsite():
    for i in a_city_url:
        try:
            temp = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
            temp_page = urlopen(temp).read()
            temp_soup = BeautifulSoup(temp_page, 'html.parser')
            result = temp_soup.select_one("a[href*=coronavirus i]")
            print(result['href'])
        except:
            continue
def find_covid():
    for i in a_city_url:
        try:
            temp = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
            temp_page = urlopen(temp).read()
            temp_soup = BeautifulSoup(temp_page, 'html.parser')
            result = temp_soup.select_one("a[href*=covid i]")
            print(i)
            print(result['href'])
            print()
        except:
            print()
            continue


find_covid()

def find_city_names():
    city_names = []
    for i in a_city_url:
        city = str.split(i, "/")[2]
        city_t = str.split(city, ".")
        # city_names.append(city)
        city_name = ""
        if len(city_t) == 3:
            city_names.append(city_t[1])
        elif len(city_t) == 2:
            city_names.append(city_t[0])
        else:
            city_names.append(city_t[2])










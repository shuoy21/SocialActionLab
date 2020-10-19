#modified from https://github.com/tcarobruce/us-mayors/blob/master/mayors.py

import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import csv

base_url = "https://www.usmayors.org/mayors/meet-the-mayors/"

def get_mayors():
    payload = {'submit': 'Search', 'searchTerm': "Texas"}
    headers = {"User-Agent": "mayors-scraper/0.0.1"}
    response = requests.post(base_url, data=payload, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.find('div', {'class':'post-content'})
    a_mayor = content.find_all('ul')
    mayors = list()
    for i in a_mayor:
        mayors.append(get_mayor_info(i))

    return mayors



def get_mayor_info(mayor): #helper
    iter = list(mayor.contents)
    mayor_data = list()
    mayor_data.append(iter[3].text)
    mayor_data.append(iter[5])
    mayor_data.append(iter[9]['href'])
    mayor_data.append(iter[13]['href'])
    return mayor_data


def write_to_csv(link, mayors):
    with open(link, mode='w') as mayor_file:
        mayor_writer = csv.writer(mayor_file, quoting=csv.QUOTE_ALL)
        for i in mayors:
            mayor_writer.writerow(i)



if __name__ == '__main__':
    mayors = get_mayors()
    write_to_csv("mayors_texas.csv", mayors)


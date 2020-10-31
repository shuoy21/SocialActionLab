import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def get_bio():
    with open("mayors_texas.csv") as csv_file:
        mayor_reader = csv.reader(csv_file)
        mayor_tx = list(mayor_reader)
    gov_link = list()
    for i in mayor_tx:
        gov_link.append(i[2])
    return gov_link

def get_covid_link (url):
    temp = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    temp_page = urlopen(temp).read()
    temp_soup = BeautifulSoup(temp_page, 'html.parser')

    covid_result = temp_soup.find_all("a", href=re.compile("covid"))
    covid_links = list()
    if len(covid_result) > 0:
        for i in covid_result:
            covid_links.append(i['href'])

    corona_result = temp_soup.find_all("a", href=re.compile("coronavirus"))
    corona_links = list()
    if len(corona_result) > 0:
        for i in covid_result:
            corona_links.append(i['href'])
    return list(set(covid_links + corona_links))

def get_covid_websites():
    url = get_bio()
    temp = {}
    for i in url:
        try:
            temp[i] = get_covid_link(i)
        except:
            temp[i] = "error"

    return temp




if __name__ == "__main__":
    dict = get_covid_websites()
    w = csv.writer(open("covid websites.csv", "w"))
    for key, val in dict.items():
        row = [key]
        for i in val:
            row.append(i)
        w.writerow(row)

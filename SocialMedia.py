import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_bio():
    with open("mayors_texas.csv") as csv_file:
        mayor_reader = csv.reader(csv_file)
        mayor_tx = list(mayor_reader)
    bio = list()
    for i in mayor_tx:
        bio.append(i[3])
    return bio


def get_twitter_and_ins(url):
    temp = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    temp_page = urlopen(temp).read()
    temp_soup = BeautifulSoup(temp_page, 'html.parser')
    ins_a = temp_soup.select_one("a[href*=instagram]")

    instagram_handle = None
    if ins_a is not None:
        instagram_handle = ins_a.get('href').split('/')[3]

    twitter_a = temp_soup.select_one("a[href*=twitter]")
    twitter_handle = None
    if twitter_a is not None:
        twitter_handle = twitter_a.get('href').split('/')[3]
    return [instagram_handle, twitter_handle]


def combine_results():
    url = get_bio()
    result = list()
    for i in url:
        try:
            result.append(get_twitter_and_ins(i))
        except:
            result.append(["error", "error"])
    return result


if __name__ == "__main__":
   results = combine_results()

   with open("mayors_texas.csv") as csv_file,\
       open("social_media.csv",'w', newline='') as w_obj:
       mayor_reader = csv.reader(csv_file)
       mayor_writer = csv.writer(w_obj)
       for row, account in zip(mayor_reader, results):
           row.append(account[0])
           row.append(account[1])
           mayor_writer.writerow(row)
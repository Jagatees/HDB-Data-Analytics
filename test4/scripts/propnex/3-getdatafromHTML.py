import os
import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession

title = []
price_house = []
links = []

# Return list of item in folder
def get_item_in_dic(x):
    txtfiles = []
    arr = os.listdir(x)
    for file in arr:
        txtfiles.append(file)
    return txtfiles

def main(x):
    list_item = get_item_in_dic(x)
    print('Length : ' + str(len(list_item)))

    counter = 0

    for index in list_item:
        # print(index)
        with open(x + "/" + str(index), "r") as f:
            doc = BeautifulSoup(f, "html.parser")

            title_of_room = doc.find_all(class_ = 'lbb-1')
            for index in title_of_room:
                counter += 1
                roomtitle = index.find('h3')['data-original-title']
                title.append(roomtitle)
                # print(roomtitle)

            price = doc.find_all(class_ = 'lbb-22')
            for index in price:
                p = index.find('h4').text
                price_house.append(p)
                # print(p)

            link = doc.findAll('div',class_='lbb-flex')
            for index in link:
                p = index.find('a', class_='lbb-2').get('href')
                p = 'https://www.propnex.com' + p
                links.append(p)
                # print(p)

    data = [
        {
            'Title': title[i],
            'Price': price_house[i],
            'Deep_Crawl_Links' : links[i],
        }
        for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("propnex_scrapping.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


main('propnex_scrapped_html')
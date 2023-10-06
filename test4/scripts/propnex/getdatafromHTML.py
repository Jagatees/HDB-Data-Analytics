import os
import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession


links = []
title = []
room_type = []

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

            title_of_room = doc.find_all(class_ = 'listingDetailTitle')
            for index in title_of_room:
                roomtitle = index.text
                roomtitle = roomtitle.replace("\n", "")
                # print(roomtitle)
                title.append(roomtitle)

            link = doc.find_all('a',class_='listingDetailTitle')
            for index in link:
                p = index.get('href')
                p = 'https://www.srx.com.sg' + p
                links.append(p)

            counter += 1
 

    data = [
        {
            'Title' : title[i],
            'Link' : links[i],
        }
        for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("propnex_scrapping.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

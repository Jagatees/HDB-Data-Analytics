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
            print(str(x + "/" + str(index)))
            doc = BeautifulSoup(f, "html.parser")


            title_of_room = doc.find_all(class_ = 'listingDetailTitle')
            print(len(title_of_room))

            for index in title_of_room:
               href = index['href']
               p = 'https://www.srx.com.sg' + href
               links.append(p)
               text = index.get_text()
               text = text.replace("\n", "")
               title.append(text)
               counter += 1

                
 
    print(len(links))
    print(counter)

    data = [
        {
            'Title' : title[i],
            'Links' : links[i],
        }
        for i in range(0, counter, 2)
        
    ]
    # Save the data as JSON
    with open("propnex_scrapping.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

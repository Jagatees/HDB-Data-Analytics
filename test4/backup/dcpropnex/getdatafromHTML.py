import os
import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession


link_website = []
data = []

# Return list of item in folder
def get_item_in_dic(x):
    txtfiles = []
    arr = os.listdir(x)
    for file in arr:
        txtfiles.append(file)
    return txtfiles

def main(x):
    list_item = get_item_in_dic(x)
    # print('Length : ' + str(len(list_item)))
    counter = 0



    for index in list_item:
        # print(index)
        with open(x + "/" + str(index), "r") as f:
            soup = BeautifulSoup(f, 'html.parser')

            split_text = soup.find('a', id='listingShareSms')['href'].split('"')
            link_website.append(split_text[-1])
            counter += 1
    



    data = [
    {
        'link' : link_website[i],
    }
    for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("deep_crawling_propnex.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


        
    

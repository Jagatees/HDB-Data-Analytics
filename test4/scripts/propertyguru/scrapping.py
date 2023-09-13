import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession


def test():
    with open("website.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")

        # Get Higest Page Count 
        page_count = doc.find(class_='kiAZx').find_all('a')[4]['aria-label'].split(' ')[1]
        # print(page_count)

        title_of_room = doc.find_all(class_ = '_12dss')
        for index in title_of_room:
            # Title 
            title_of_room = index.find(class_ = '_3FkoX')
            title_of_room = title_of_room.find('a')['title']
            print(title_of_room)

            # Price
            price_of_room = index.find(class_ = '_3XjHl')
            price_of_room = price_of_room.find_all('li')[1]['content'].split('/')[0][1:].replace(',','')
            print(price_of_room)

            # Link to Full Page
            link_to_room = index.find(class_ = '_3FkoX')
            link_to_room = 'https://www.99.co' + link_to_room.find('a')['href']
            print(link_to_room)



test()


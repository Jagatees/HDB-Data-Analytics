import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession
from multiprocessing import cpu_count, Pool, freeze_support, Lock

type_room = []
title_room = []
links_room = []
sub_heading_room = []
description_room = []
price_list_room = []
day = []
month = []
year = []


FIRST_PAGE_NUMBER = 1

def get_request_home_page_website(website):
    return requests.get(website)

def get_content_website(soup, element, _class):
    return soup.find(element, class_=_class)

def count_max_page(page_count):
    return math.ceil(int(page_count.get_text()) / 10)


# Deep Crawling
dc_title = []
dc_description = []
dc_location = []
dc_details = []
links_testing = []
day = []
month = []
year = []

# Create a lock to synchronize file writes
file_lock = Lock()

def store_url():
    with open('test.json', 'r') as json_file:
        file_data = json.load(json_file)

        urls_y = []
        for index in file_data:
            urls_y.append(index['Links'])
        return urls_y

def content_html(url):
    page = requests.get(url)
    links_testing.append(str(url))
    soup = BeautifulSoup(page.text, "html.parser")
    response = requests.get(url)

    if response.status_code == 200:
        title_fp = soup.find('h1')
        dc_title.append(title_fp.get_text() if title_fp else "")

        room_details_div = soup.find('div', class_='room-details')
        li_elements = room_details_div.find_all('li')
        li_text_list = [li.get_text() for li in li_elements]
        dc_details.append(li_text_list)
        time = dc_details[0][0].split('on ', 1)[1].split('.')
        day.append(time[0])
        month.append(time[1])
        year.append(time[2])

        location_fp = soup.find(class_='room-street')
        dc_location.append(location_fp.get_text() if location_fp else "")

        description_elements = soup.find(class_='room-description')
        description_text = description_elements.get('description-text')
        dc_description.append(description_text)
  

def deep_crawl(url):
    content_html(url)
    deep_crawling_data = [
        {
            'UID': str(i),
            'Title': dc_title[i],
            'Location': dc_location[i],
            'Tags': dc_details[i],
            'Links': links_testing[i],
            'Description': dc_description[i],
            'Day': day[i],
            'Month': month[i],
            'Year': year[i]
        }
        for i in range(len(dc_title))
    ]

    # print(len(dc_title))
    with file_lock:
        with open("deep_crawl.json", "w") as json_file:
            json.dump(deep_crawling_data, json_file, indent=4)



def main():
    freeze_support()
    
    print('starting')
    
    start = time.perf_counter()
    with Pool(cpu_count()) as p:
        p.map(deep_crawl, store_url())
    fin = time.perf_counter() - start
    print('Time Taken for Deep Crawling: ' + str(fin))

if __name__ == '__main__':
    main()
    

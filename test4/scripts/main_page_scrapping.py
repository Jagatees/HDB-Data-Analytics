import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession

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


def get_request_page_range(int):
    urls_x = []
    for index in range(1, int):
        urls_x.append(
            f'https://rentinsingapore.com.sg/rooms-for-rent/page-{index}')
    return urls_x


async def element_scrapping(s, index):
    page = await s.get(index)
    soup = BeautifulSoup(page.text, "html.parser")

    if page.status_code == 200:
        room_wide_listing_container = soup.find_all(
            'div', class_='room__wide listing-container')
        room_sub_location = soup.find_all(
            'h3', class_='room-sublocation mobile-room-sublocation')
        price = soup.find_all('div', class_='room-price')
        for div in room_sub_location:
            remove_text = div.get_text()
            remove_text = remove_text.strip().split('-')
            type_room.append(remove_text[0])
            title_room.append(remove_text[1])
        for div in room_wide_listing_container:
            a_tags_link = div.find_all('a')
            for a_tag in a_tags_link:
                link = 'https://rentinsingapore.com.sg/rooms-for-rent' + \
                    a_tag['href']
                links_room.append(link)
                a_tags_title = a_tag['title']
                sub_heading_room.append(a_tags_title)
        for div in price:
            price_text = div.get_text().strip()
            price_list_room.append(price_text)
    else:
        None

    data = [
        {
            'UID': i,  # Assign a UID based on the index 'i'
            'Price': price_list_room[i],
            'Type': type_room[i],
            'Title': title_room[i],
            'Links': links_room[i],
            'Sub Heading': sub_heading_room[i],

        }
        for i in range(len(title_room))
    ]

    # Save the data as JSON
    with open("main_page.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


async def main_scrapping():
    # Get Total Page Number <-- Start
    request_web = get_request_home_page_website(
        'https://rentinsingapore.com.sg/rooms-for-rent')
    soup = BeautifulSoup(request_web.text, "html.parser")

    total_count = get_content_website(soup, 'span', 'total-count')
    max_number_page = count_max_page(total_count)

    x = get_request_page_range(max_number_page)

    s = AsyncHTMLSession()
    tasks = (element_scrapping(s, url) for url in x)
    return await asyncio.gather(*tasks)


print('starting')
start = time.perf_counter()
asyncio.run(main_scrapping())
fin = time.perf_counter() - start
print('Time Taken : ' + str(fin))



import os
import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession

beds_list = []
baths_list = []
numbers_and_sqft_list = []
title = []
deep_crawlling_link = []


counter = 0

# Return list of item in folder
def get_item_in_dic(x):
    txtfiles = []
    arr = os.listdir(x)
    for file in arr:
        txtfiles.append(file)
    return txtfiles

def main(x):
    counter = 0

    list_item = get_item_in_dic(x)
    print('Length : ' + str(len(list_item)))

    target_image_sources = [
    '/img/listing/ic_baths.png',
    '/img/listing/ic_beds.png',
    '/img/listing/ic_sqft.png',
    '/img/listing/ic_location.png'
    ]

    for index in list_item:
        # print(index)
        with open(x + "/" + str(index), "r") as f:
            soup = BeautifulSoup(f, 'html.parser')

            

            parent_element = soup.find('div', class_='lbb-21')
            if parent_element is not None:

                # Get hyperlink  
                link_element = soup.find('link', rel='canonical')
                href = link_element.get('href')
                deep_crawlling_link.append(href)


                # Extract Bullet Point from Stats
                li_elements = parent_element.find_all('li')
                if len(li_elements) == 4:
                    counter = counter + 1
                    for index in range(len(li_elements)):
                        img_tag = li_elements[index].find('img', {'class': 'img img-fluid'})
                        src = img_tag.get('src')
                        print(src)
                        text = li_elements[index].get_text(strip=True)
                        print(text)

                        if src == target_image_sources[0]:
                            baths_list.append(text)
                        if src == target_image_sources[1]:
                            beds_list.append(text)
                        if src == target_image_sources[2]:
                            numbers_and_sqft_list.append(text)
                        if src == target_image_sources[3]:
                            title.append(text)


                if len(li_elements) <= 3:
                    counter = counter + 1
                    bathsIsTrue, bedIsTrue, roomIstrue, titleIstitle = False, False, False, False
                    for index in range(len(li_elements)):
                        img_tag = li_elements[index].find('img', {'class': 'img img-fluid'})
                        src = img_tag.get('src')
                        print(src)
                        text = li_elements[index].get_text(strip=True)
                        print(text)

                        if src == target_image_sources[0]:
                            baths_list.append(text)
                            bathsIsTrue = True
                        if src == target_image_sources[1]:
                            beds_list.append(text)
                            bedIsTrue = True
                        if src == target_image_sources[2]:
                            numbers_and_sqft_list.append(text)
                            roomIstrue = True
                        if src == target_image_sources[3]:
                            title.append(text)
                            titleIstitle = True

                    if bathsIsTrue != True:
                        baths_list.append("empty")
                    if bedIsTrue != True:
                        beds_list.append("empty")
                    if roomIstrue != True:
                        numbers_and_sqft_list.append("empty")
                    if titleIstitle != True:
                        title.append("empty")


                    
                    

                    



    data = [
        {
            'Baths': baths_list[i],
            'Beds': beds_list[i],
            'Sqft' : numbers_and_sqft_list[i], 
            'Deep_Crawling' : deep_crawlling_link[i],
            'Title': title[i]
        }
        for i in range(counter)
        
    ]

    print(str(counter))
    # Save the data as JSON
    with open("deep_crawling_propnex_scrapping.json", "w") as json_file:
        json.dump(data, json_file, indent=4)   
        
    
main('deep_crawling_propnex_scrapped_html')
print(len(beds_list))
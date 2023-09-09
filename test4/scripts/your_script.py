from bs4 import BeautifulSoup
import json
import math
import requests

type_room = []
title_room = []
links_room = []
sub_heading_room = []
description_room = []
price_list_room = []


def scrapping():
    url = 'https://rentinsingapore.com.sg/rooms-for-rent'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
       
    total_count = soup.find('span', class_= 'total-count')

    # Max Page Count
    max_number_page = math.ceil(int(total_count.get_text()) / 10)
    print(max_number_page)

    for page in range(1):
        url = f'https://rentinsingapore.com.sg/rooms-for-rent/page-{page}'
        print('at page ' + str(page))
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")

        # Convert to Function and return the list args (str, str)
        room_wide_listing_container = soup.find_all('div', class_='room__wide listing-container')
        room_sub_location = soup.find_all('h3', class_='room-sublocation mobile-room-sublocation')
        price = soup.find_all('div', class_='room-price')  

        for div in room_sub_location:
            remove_text = div.get_text()
            remove_text = remove_text.strip().split('-')
            type_room.append(remove_text[0])
            title_room.append(remove_text[1])
            

        for div in room_wide_listing_container:
            a_tags_link = div.find_all('a')
            for a_tag in a_tags_link:
                link = 'https://rentinsingapore.com.sg/rooms-for-rent' + a_tag['href']
                links_room.append(link)
                a_tags_title = a_tag['title']
                sub_heading_room.append(a_tags_title)
            

        for div in price:
            price_text = div.get_text().strip()
            price_list_room.append(price_text)
           

    data = [
    {
        'UID': i,  # Assign a UID based on the index 'i'
        'Price': price_list_room[i],
        'Type': type_room[i],
        'Title': title_room[i],
        'Links': links_room[i],
        'Sub Heading': sub_heading_room[i],
        'Description': 'DID NOT GET IT',
        'Tags': ['tags' , 'tags' , 'tags', 'tags']
        
    }
    for i in range(len(title_room))
]

    # Save the data as JSON
    with open("output.json", "w") as json_file:
            json.dump(data, json_file, indent=4)


# Description 
# Room Details 
# Location 
# Date of posting

def deepCrawling():
    dc_title = []
    dc_description = []
    dc_location = []
    dc_details = []
    newstatment = []

    with open('output.json', 'r') as json_file:
        # Load the JSON data into a Python data structure
        file_data = json.load(json_file)

        for i in range(1):
            url = file_data[i]['Links']
            page = requests.get(url).text
            soup = BeautifulSoup(page, "html.parser")

            print('starting')

            # Title
            title_fp = soup.find('h1')
            dc_title.append(title_fp.get_text() if title_fp else "")
            print(dc_title)

           

            # Location
            location_fp = soup.find(class_='room-street')
            dc_location.append(location_fp.get_text() if location_fp else "")
            print(dc_location)

            # Description
            description_elements = soup.find(class_='room-description')

            for element in description_elements:
                description_text = element.get('description-text')
                if description_text:
                    start_index = description_text.find("'") + 1
                    extracted_text = description_text[start_index:]
                    dc_description.append(extracted_text)


            
            # Room Details 
            room_details_div = soup.find('div', class_='room-details')
            print(room_details_div)
            for x in room_details_div:
                bullet = x.get('room-details')
            print(bullet)
           
         
           
          

    # deep_crawling_data = [
    #     {
    #         'Title': dc_title[i],
    #         'Location': dc_location[i],
    #         'Description': dc_description[i],
    #         'Details': dc_details[i]
    #     }
    #     for i in range(len(dc_title))
    # ]

    # # Save the data as JSON
    # with open("deep_crawl.json", "w") as json_file:
    #     json.dump(deep_crawling_data, json_file, indent=4)

            

    

            
deepCrawling()
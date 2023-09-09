from bs4 import BeautifulSoup
import json
import math
import requests

title = []
links = []
sub_heading = []
description = []
price_list = []

data = {
        'Title': [],
        'Links': [],
        'Sub Heading': [],
        'Description': [],
        'Price': []
    }


# https://rentinsingapore.com.sg/rooms-for-rent
# https://rentinsingapore.com.sg/rooms-for-rent/page-1
# https://rentinsingapore.com.sg/ID679822


def displayText():
    with open("web_site_test.html", "r") as f: # switch to website link
        soup = BeautifulSoup(f, "html.parser")
       
        total_count = soup.find('span', class_= 'total-count')

        # Max Page Count
        max_number_page = math.ceil(int(total_count.get_text()) / 10)
        print(max_number_page)

        for page in range(2):
            url = f'https://rentinsingapore.com.sg/rooms-for-rent/page-{page}'
            print('at page ' + str(page))
            page = requests.get(url).text
            soup = BeautifulSoup(page, "html.parser")

            # Convert to Function and return the list args (str, str)
            room_wide_listing_container = soup.find_all('div', class_='room__wide listing-container')
            room_sub_location = soup.find_all('h3', class_='room-sublocation mobile-room-sublocation')
            room_description = soup.find_all('p', class_='room-description')
            price = soup.find_all('div', class_='room-price')

            for div in room_sub_location:
                remove_text = div.get_text()
                remove_text = remove_text.strip()
                title.append(remove_text)
            

            for div in room_wide_listing_container:
                a_tags_link = div.find_all('a')
                for a_tag in a_tags_link:
                    link = 'https://rentinsingapore.com.sg/rooms-for-rent' + a_tag['href']
                    links.append(link)
                    a_tags_title = a_tag['title']
                    sub_heading.append(a_tags_title)

            # Clean Description
            for div in room_description:
                description.append(div.get_text())
            

            for div in price:
                price_text = div.get_text().strip()
                price_list.append(price_text)
           

    data = [
        {
            'Title': title[i],
            'Links': links[i],
            'Sub Heading': sub_heading[i],
            'Description': description[i],
            'Price': price_list[i]
        }
        for i in range(len(title))
    ]

    # Save the data as JSON
    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


# Description 
# Room Details 
# Location 
# Date of posting

dc_title = []


def deepCrawling():
    with open('output.json', 'r') as json_file:
    # Load the JSON data into a Python data structure
        file_data = json.load(json_file)

        for i in range(len(file_data)):
            url = file_data[i]['Links']
            # print(url)
            page = requests.get(url).text
            soup = BeautifulSoup(page, "html.parser")

            # Title
            title_fp = soup.find('h1')
            dc_title.append(title_fp.get_text())
           

       



            

    

            

deepCrawling()
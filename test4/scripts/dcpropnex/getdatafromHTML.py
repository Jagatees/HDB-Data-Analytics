import os
import time
from bs4 import BeautifulSoup
import json
import math
import requests
import asyncio
from requests_html import AsyncHTMLSession


# Create an empty list for each bullet point category
address_list = []
property_type = []
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

            element = soup.find('a', id='listingShareEm')
            counter += 1
            # Extract the 'href' attribute value
            if element and 'href' in element.attrs:
                href_value = element['href']
                link_website.append(href_value)
                print(href_value)
            else:
                link_website.append('None')
                print("No href attribute found.")




            
            elements = soup.find_all(class_ = 'listing-about-main-value')

            print(len(elements))
            
            # Extract and print the values
            for element in elements:
                if element.get('id') == 'listing-name':
                    counter += 1
                    value = element.get_text(strip=True)
                    address_list.append(value)
                elif element.get('id') != 'listing-name':
                    counter += 1
                    address_list.append("None")

                if element.get('id') == 'property-type':
                    counter += 1
                    value = element.get_text(strip=True)
                    property_type.append(value)
                elif element.get('id') != 'property-type':
                    counter += 1
                    property_type.append("None")


            # DO DEEP CRAWLING HERE

    data = [
    {
        'link' : link_website[i],
    }
    for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("deep_crawling_propnex.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


        
    

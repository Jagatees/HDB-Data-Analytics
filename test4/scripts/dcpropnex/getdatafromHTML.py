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
property_name_list = []
property_type_list = []
bedrooms_list = []
bathrooms_list = []
furnish_list = []
tenure_list = []
developer_list = []
built_year_list = []
hdb_town_list = []
asking_list = []
size_list = []
psf_list = []
tenancy_status_list = []
date_listed_list = []
counter = 0

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


    for index in list_item:
        # print(index)
        with open(x + "/" + str(index), "r") as f:
            soup = BeautifulSoup(f, 'html.parser')


            value_elements = soup.find_all(class_='listing-about-main-value')

            for element in value_elements:
                value = element.get_text(strip=True)
                if "Address" in element.attrs.get('itemprop', ''):
                    address_list.append(value)
                elif "Property Name" in element.attrs.get('itemprop', ''):
                    property_name_list.append(value)
                elif "Property Type" in element.attrs.get('itemprop', ''):
                    property_type_list.append(value)
                elif "Bedrooms" in element.attrs.get('itemprop', ''):
                    bedrooms_list.append(value)
                elif "Bathrooms" in element.attrs.get('itemprop', ''):
                    bathrooms_list.append(value)
                elif "Furnish" in element.attrs.get('itemprop', ''):
                    furnish_list.append(value)
                elif "Tenure" in element.attrs.get('itemprop', ''):
                    tenure_list.append(value)
                elif "Developer" in element.attrs.get('itemprop', ''):
                    developer_list.append(value)
                elif "Built Year" in element.attrs.get('itemprop', ''):
                    built_year_list.append(value)
                elif "HDB Town" in element.attrs.get('itemprop', ''):
                    hdb_town_list.append(value)
                elif "Asking" in element.get_text():
                    asking_list.append(value)
                elif "Size" in element.attrs.get('itemprop', ''):
                    size_list.append(value)
                elif "PSF" in element.attrs.get('itemprop', ''):
                    psf_list.append(value)
                elif "Tenancy Status" in element.attrs.get('itemprop', ''):
                    tenancy_status_list.append(value)
                elif "Date Listed" in element.attrs.get('itemprop', ''):
                    date_listed_list.append(value)



# Print the lists
print("Address:", address_list)
print("Property Name:", property_name_list)
print("Property Type:", property_type_list)
print("Bedrooms:", bedrooms_list)
print("Bathrooms:", bathrooms_list)
print("Furnish:", furnish_list)
print("Tenure:", tenure_list)
print("Developer:", developer_list)
print("Built Year:", built_year_list)
print("HDB Town:", hdb_town_list)
print("Asking:", asking_list)
print("Size:", size_list)
print("PSF:", psf_list)
print("Tenancy Status:", tenancy_status_list)
print("Date Listed:", date_listed_list)
          


counter = 3


# Create a list of dictionaries for each property
data = []
for i in range(counter):
    property_data = {
        'Address': 'none',
        'PropertyName': 'none',
        'PropertyType': 'none',
        'Bedrooms': 'none',
        'Bathrooms': 'none',
        'Furnish': 'none',
        'Tenure': 'none',
        'Developer': 'none',
        'BuiltYear': 'none',
        'HDBTown': 'none',
        'Asking': 'none',
        'Size': 'none',
        'PSF': 'none',
        'TenancyStatus': 'none',
        'DataListed': 'none'
    }
    data.append(property_data)

# Save the data as JSON
with open("deep_crawling_propnex_scrapping.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
        
    

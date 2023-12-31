import os
from bs4 import BeautifulSoup
import json
from datetime import datetime

'''
    Initialize Init 
'''
title = []
room_type_title = []
address = []
price = []
link = []
type_ = []
num_beds = []
num_toilet = []
lease = []
sqrt_feet = []
yearbuilt = []
remaingyear = []

'''
    Args : int
    Description : Return list of item in folder
'''
def get_item_in_dic(x):
    txtfiles = []
    arr = os.listdir(x)
    for file in arr:
        txtfiles.append(file)
    return txtfiles



'''
    Args : int
    Description : Scrap Website for elements and output to json file
'''
def main(x):
    list_item = get_item_in_dic(x)
    print('Length : ' + str(len(list_item)))

    counter = 0

    for index in list_item:
        print(index)
        with open(x + "/" + str(index), "r") as f:
            doc = BeautifulSoup(f, "html.parser")

            title_of_room = doc.find_all(class_ = '_12dss')
            for index in title_of_room:
                # Title 
                title_of_room = index.find(class_ = '_3FkoX')
                title_of_room = title_of_room.find('a')['title']
                title.append(title_of_room)

                # Break_Down_Title - Location
                title_of_room = index.find(class_ = '_3FkoX')
                title_of_room = title_of_room.find('a')['title'].split('in')
                room_type_title.append(title_of_room[0])
                address.append(title_of_room[1])

                # Price
                price_of_room = index.find(class_ = '_3XjHl')
                price_of_room = price_of_room.find_all('li')[1]['content'].split('/')[0][1:].replace(',','')
                # print(price_of_room)
                price.append(price_of_room)

                # Link to Full Page
                link_to_room = index.find(class_ = '_3FkoX')
                link_to_room = 'https://www.99.co' + link_to_room.find('a')['href']
                # print(link_to_room)
                link.append(link_to_room)


                # Type of Room
                room_type = index.find('li', class_='_1LPAx', itemprop='accommodationCategory')
                room_type = room_type.text
                # print(room_type)
                type_.append(room_type)

                # X Beds
                beds = index.find('li', class_='_1x-U1', itemprop='numberOfBedrooms')
                if beds != None:
                    beds = beds.text.replace('\n','').replace(" ", "").replace("Beds", "")
                    # print(beds)
                    num_beds.append(beds)
                else:
                    # print('None')
                    num_beds.append('None')


                # X toilet
                toilet = index.find('li', class_='_1x-U1', itemprop='numberOfBathroomsTotal')
                if toilet != None:
                    toilet = toilet.text.replace('\n','').replace(" ", "").replace("Baths", "").replace("Bath", "")
                    # print(beds)
                    num_toilet.append(toilet)
                else:
                    # print('None')
                    num_toilet.append('None')


                 # Lease
                le = index.find('li', itemprop='leaseLength')
                if le != None:
                    # print(le.text)
                    lease.append(le.text)
                else: 
                    # print('None')
                    lease.append('None')

                # Sqrt Feet Floor
                le = index.find('li', itemprop='floorSize')
                if le != None:
                    text = le.text
                    output = text.split('/')                    
                    sqft_part = output[0]
                    sqft_part = sqft_part.replace('sqft', '').strip()
                    sqrt_feet.append(sqft_part)
                else: 
                    # print('None')
                    sqrt_feet.append('None')




                 # yearbuilt
                le = index.find('li', itemprop='yearbuilt')
                if le != None:
                    # print(le.text)
                    yearbuilt.append(le.text)
                    last = datetime.now().year - int(le.text)
                    remaingyear.append(last)
                else: 
                    # print('None')
                    remaingyear.append('None')
                    yearbuilt.append('None')


                counter = counter + 1




    data = [
        {
            'Title': title[i],
            'Room_Type' : room_type_title[i],
            'Full Address' : address[i],
            'Price': price[i],
            'Link': link[i],
            'Type' : type_[i],
            'Num_Bed' : num_beds[i],
            'Num_Toilet' : num_toilet[i],
            'Lease' : lease[i],
            'Yearbuilt' : yearbuilt[i],
            'YearLeft' : remaingyear[i],
            'Sqft' : sqrt_feet[i],

        }
        for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("centralized/99co/json/nintynine_scrap.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


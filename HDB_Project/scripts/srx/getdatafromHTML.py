import datetime
import os
from bs4 import BeautifulSoup
import json
from datetime import datetime

'''
    Initialize Init 
'''
links = []
title = []
bed_numbers = []
toilet_numbers = []
size_house = []
room = []
model = []
built_year = []
price_list = []
reaming_lease = []

year = datetime.now().year


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
        # print(index)
        with open(x + "/" + str(index), "r") as f:
            print(str(x + "/" + str(index)))
            doc = BeautifulSoup(f, "html.parser")


            price = doc.find_all(class_ = 'listingDetailPrice')
            for index in price:
                text = index.get_text()
                price_list.append(text.strip().replace('$', '').replace(',', ''))


            title_of_room = doc.find_all(class_ = 'listingDetailTitle')
            print(len(title_of_room))

            for index in range(0, len(title_of_room), 2):
               href = title_of_room[index]['href']
               p = 'https://www.srx.com.sg' + href
               links.append(p)
               text = title_of_room[index].get_text()
               text = text.replace("\n", "")
               title.append(text)
               counter += 1   


            bath_bed = doc.find_all(class_ = 'listingDetailRoomContainer')
            for index in bath_bed:
                bed = index.find(class_='listingDetailRoomNo')
                bath = index.find(class_='listingDetailToiletNo')

                # Check if room_element is None and append "None" or the extracted text
                if bed is None:
                    bed_numbers.append("None")
                else:
                    bed_numbers.append(bed.text.strip())

                # Check if toilet_element is None and append "None" or the extracted text
                if bath is None:
                    toilet_numbers.append("None")
                else:
                    toilet_numbers.append(bath.text.strip())

            size = doc.find_all(class_ = 'listingDetailValues')
            for index in size:
                text = index.get_text()
                size_house.append(text.split(' ')[0].strip())

            houselistype = doc.find_all(class_ = 'listingDetailType')
            for index in houselistype:
                text = index.get_text()
                split_text = text.split('•')

                # Work on 2 or 1 length value 
                if len(split_text) == 3:
                    room.append(split_text[0].strip())
                    model.append(split_text[1].strip())
                    test = split_text[2].strip().split('-')
                    if len(test) > 1:
                        built_year.append(test[1])
                        reaming_lease.append(str(year - int(test[1])))
                    else:
                        reaming_lease.append('None')
                        built_year.append('None')
                else:
                    room.append('None')
                    model.append('None')
                    built_year.append('None')
                    reaming_lease.append('None')

                   


 
    print(len(links))
    print(counter)

    data = [
        {
            'Title' : title[i],
            'Link' : links[i],
            'Bed' : bed_numbers[i],
            'Toilet' : toilet_numbers[i],
            'Size' : size_house[i],
            'Room' : room[i],
            'Model' : model[i],
            'Built' : built_year[i],
            'Price' : price_list[i],
            'Remaing' : reaming_lease[i]
        }
        for i in range(counter)
        
    ]
    # Save the data as JSON
    with open("centralized/srx/json/srx_scrapping.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

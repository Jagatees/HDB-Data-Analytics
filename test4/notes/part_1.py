def deepCrawling():
    dc_title = []
    dc_description = []
    dc_location = []
    dc_details = []
    links_testing = []

    with open('scrap.json', 'r') as json_file:
        # Load the JSON data into a Python data structure
        file_data = json.load(json_file)

        try:
            for i in range(50): 
                url = file_data[i]['Links']
                page = requests.get(url).text
                links_testing.append(str(url))
                soup = BeautifulSoup(page, "html.parser")    
                response = requests.get(url)            
                print('Index '+ str(i) + 'Scrapping @' + str(url))
            
                if response.status_code == 200:
                    print()
                    # Title
                    title_fp = soup.find('h1')
                    dc_title.append(title_fp.get_text() if title_fp else "")
                    # print(dc_title)
        
                    # Room Details 
                    room_details_div = soup.find('div', class_='room-details')
                    li_elements = room_details_div.find_all('li')
                    li_text_list = [li.get_text() for li in li_elements]
                    # print(li_text_list)
                    dc_details.append(li_text_list)
                    time = dc_details[0][0].split('on ', 1)[1].split('.')
                    day.append(time[0])
                    month.append(time[1])
                    year.append(time[2])
                    # print(dc_details)

                    # Location
                    location_fp = soup.find(class_='room-street')
                    dc_location.append(location_fp.get_text() if location_fp else "")
                    # print(dc_location)

                    # Description
                    description_elements = soup.find(class_='room-description')
                    description_text = description_elements.get('description-text')
                    dc_description.append(description_text)
                    # print(dc_description)
                else:
                    continue   
        except:
            pass
    deep_crawling_data = [
        {
        'UID' : str(i),
        'Title': dc_title[i],
        'Location': dc_location[i],
        'Tags': dc_details[i],
        'Links' : links_testing[i],
        'Description': dc_description[i],
        'Day' : day[i],
        'Month' : month[i],
        'Year' : year[i]

        }
        for i in range(len(dc_title))
    ]

    # Save the data as JSON
    with open("deep_crawl.json", "w") as json_file:
        json.dump(deep_crawling_data, json_file, indent=4)

    

start = time.perf_counter()
# asyncio.run(main_scrapping())
deepCrawling()
fin = time.perf_counter() - start
print('Time Taken : ' + str(fin))

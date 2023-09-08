from bs4 import BeautifulSoup

def displayText():
    with open("web_site_test.html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        room_wide_listing_container = soup.find_all('div', class_='room__wide listing-container')
        room_sub_location = soup.find_all('h3', class_='room-sublocation mobile-room-sublocation')
        room_description = soup.find_all('p', class_='room-description')
        price = soup.find_all('div', class_='pull-right')


        # Title 
        print('Title')
        for div in room_sub_location:
            print(div.get_text())

        print('Links')
        # Links (Mising Append + to add to make full link)
        for div in room_wide_listing_container:
            a_tags_link = div.find_all('a')
            
            for a_tag in a_tags_link:
                link = a_tag['href']
                print(link)

        print('Sub Heading')
        # Sub Heading
        for div in room_wide_listing_container:
            a_tags_link = div.find_all('a')

            for a_tag in a_tags_link:
                a_tags_title = a_tag['title']
                print(a_tags_title)

        print('Description')
        # Sub Heading
        for div in room_description:
            print(div.get_text())
            print('\n')

        # Price (remove free to contact from the data)
        print('Price')
        for div in price:
            print(div.get_text())

       
            

displayText()
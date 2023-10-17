from bs4 import BeautifulSoup
from selenium import webdriver
import os

'''
    Description : Get the max page count from the website
'''
def main():
    driver = webdriver.Chrome()
    url = 'https://www.99.co/singapore/s/rent?bathrooms=any&building_age=any&composite_floor_level=any&composite_furnishing=any&composite_views=any&features_and_amenities=any&has_floor_plan=false&isFilterUnapplied=false&listing_type=rent&main_category=all&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&path=%2Fsingapore%2Frent&period_of_availability=any&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&rental_type=all&rooms=any&show_cluster_preview=true&show_description=true&show_future_mrts=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11'
    driver.get(url)
    driver.implicitly_wait(10)  
    html_content = driver.page_source
    driver.quit()
    file_path = 'pagecount.html'

    with open(file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    with open("pagecount.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")
        page_count = doc.find(class_='kiAZx').find_all('a')[4]['aria-label'].split(' ')[1]
        os.remove("pagecount.html")
        return page_count
    
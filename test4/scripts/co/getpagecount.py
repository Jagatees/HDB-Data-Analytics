from bs4 import BeautifulSoup
from selenium import webdriver
import os

def main():
    # Set the path to the Chrome WebDriver executable
    chrome_driver_path = '/Users/jagatees/Downloads/chromedriver'


    # options=chrome_options
    driver = webdriver.Chrome()
  

    # Open the URL
    url = 'https://www.99.co/singapore/s/rent?bathrooms=any&building_age=any&composite_floor_level=any&composite_furnishing=any&composite_views=any&features_and_amenities=any&has_floor_plan=false&isFilterUnapplied=false&listing_type=rent&main_category=all&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&path=%2Fsingapore%2Frent&period_of_availability=any&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&rental_type=all&rooms=any&show_cluster_preview=true&show_description=true&show_future_mrts=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11'
    driver.get(url)

    # Wait for the page to load completely (you can adjust the timeout as needed)
    driver.implicitly_wait(10)  # Implicitly wait up to 10 seconds (adjust as needed)

    # Get the HTML content of the entire webpage
    html_content = driver.page_source

    # Close the WebDriver
    driver.quit()

    # Define the path for the HTML file
    html_file_path = 'pagecount.html'

    # Write the entire HTML content to the file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Entire HTML page has been saved to {html_file_path}")

    with open("pagecount.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")
        # Get Higest Page Count 
        page_count = doc.find(class_='kiAZx').find_all('a')[4]['aria-label'].split(' ')[1]
        print(page_count)
        os.remove("pagecount.html")
        return page_count
    
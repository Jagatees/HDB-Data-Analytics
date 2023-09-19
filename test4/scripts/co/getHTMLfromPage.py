import asyncio
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import threading

PAGE_NUMBER = 228
# Set the path to the Chrome WebDriver executable

WEBSITE_MAIN = 'https://www.99.co/singapore/s/sale?bathrooms=any&building_age=any&composite_floor_level=any&composite_furnishing=any&composite_views=any&features_and_amenities=any&has_floor_plan=false&isFilterUnapplied=false&main_category=hdb&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num=1&page_size=35&path=%2Fsingapore%2Fs%2Frent&period_of_availability=any&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&rental_type=all&rooms=any&show_cluster_preview=true&show_description=true&show_future_mrts=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11'

urls_X = []
threads = []


def storeallurl(x):
    for index in range(1, x + 1):
        urls_X.append(f'https://www.99.co/singapore/s/sale?bathrooms=any&building_age=any&composite_floor_level=any&composite_furnishing=any&composite_views=any&features_and_amenities=any&has_floor_plan=false&isFilterUnapplied=false&main_category=hdb&map_bounds=1.5827095153768858%2C103.49449749970108%2C1.1090706240313446%2C104.12483807587296&page_num={index}&page_size=35&path=%2Fsingapore%2Fs%2Frent&period_of_availability=any&property_segments=residential&query_coords=1.3039947%2C103.8298507&query_limit=radius&query_type=city&rental_type=all&rooms=any&show_cluster_preview=true&show_description=true&show_future_mrts=true&show_internal_linking=true&show_meta_description=true&show_nearby=true&zoom=11')

def GetHTMLPAGE(url, output):
    chrome_driver_path = '/Users/jagatees/Downloads/chromedriver'

    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)

    driver.implicitly_wait(10)  # Implicitly wait up to 10 seconds (adjust as needed)

    # Get the HTML content of the entire webpage
    html_content = driver.page_source

    # Close the WebDriver
    driver.quit()

    html_file_path = output
    
    # Write the entire HTML content to the file
    with open(output, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Entire HTML page has been saved to {html_file_path}")

# Function to scrape a chunk of URLs
def scrape_urls(urls_chunk, thread_num):
    for i, url in enumerate(urls_chunk):
        output_path = f'page_scrape/page-{thread_num}-{i}.html'
        GetHTMLPAGE(url, output_path)
    


def main(pagelength):
    storeallurl(pagelength)

    start = time.perf_counter()

    # after 4 still same time , becuase the website still need time to load
    num_threads = 4 

    chunk_size = len(urls_X) // num_threads
    url_chunks = [urls_X[i:i+chunk_size] for i in range(0, len(urls_X), chunk_size)]
    
    threads = []
    for i, url_chunk in enumerate(url_chunks):
        thread = threading.Thread(target=scrape_urls, args=(url_chunk, i + 1))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    fin = time.perf_counter() - start
    print('Time Taken : ' + str(fin))
    return ('Completed scrapping done in :' + str(fin))



    

   



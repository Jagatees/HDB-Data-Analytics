import asyncio
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import threading
import os



urls_X = []
threads = []

def storeallurl(x):
    for index in range(1, x + 1):
        urls_X.append(f'https://www.propnex.com/buy?propertyType=HDB&sortBy=newest&listingType=SALE&typeOfSale=Resale&pageNumber={index}')

def GetHTMLPAGE(url, output):
    chrome_driver_path = '/Users/jagatees/Downloads/chromedriver'

    # Options - look into the lib to see the options
    # idsable image on website 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # options=chrome_options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the URL
    driver.get(url)

    # driver.implicitly_wait(10)  # Implicitly wait up to 10 seconds (adjust as needed)

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
    if not os.path.exists("propnex_scrapped_html"):
        os.makedirs("propnex_scrapped_html")
    for i, url in enumerate(urls_chunk):
        output_path = f'propnex_scrapped_html/page-{thread_num}-{i}.html'
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


main(59)



    

   



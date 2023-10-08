# Importing Time module for timing calculation
import time
# Importing Selenium module for web scraping
from selenium import webdriver
# Importing Threading module for multi-threading
import threading
# Importing OS module for system-related operations
import os


'''
    Initialize Init 
'''
urls_X = []
threads = []

'''
    Args : Int
    Description : Store all URL into array for 99co website 
'''
def storeallurl(x):
    for index in range(1, x + 1):
        urls_X.append(f'https://www.srx.com.sg/singapore-property-listings/hdb-for-sale?page={index}')

'''
    Args : String, String
    Description : Extract HTML from 99co website save to Folder 
'''
def GetHTMLPAGE(url, output):

    # Options - look into the lib to see the options
    # idsable image on website 
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # driver.implicitly_wait(10)  # Implicitly wait up to 10 seconds (adjust as needed)

    html_content = driver.page_source
    driver.quit()
    html_file_path = output
    with open(output, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

'''
    Args : Int, Int
    Description : Create Folder for storing scrapping and json and saving html page into html
'''
def scrape_urls(urls_chunk, thread_num):
    if not os.path.exists("centralized/srx/scrapping"):
        os.makedirs("centralized/srx/scrapping")
        os.makedirs("centralized/srx/json")
    for i, url in enumerate(urls_chunk):
        output_path = f'centralized/srx/scrapping/page-{thread_num}-{i}.html'
        GetHTMLPAGE(url, output_path)
    

'''
    Args : Int
    Description : Take in page count and split scrapping process into threads  
'''
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




    

   



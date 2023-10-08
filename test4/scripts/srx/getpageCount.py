from bs4 import BeautifulSoup
from selenium import webdriver
import os


'''
    Description : Get the max page count from the website
'''
def main():

    driver = webdriver.Chrome()
    url = 'https://www.srx.com.sg/singapore-property-listings/hdb-for-sale?page=1'
    driver.get(url)

    driver.implicitly_wait(10)  # Implicitly wait up to 10 seconds (adjust as needed)
    html_content = driver.page_source
    driver.quit()
    html_file_path = 'pagecount.html'

    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    with open("pagecount.html", "r") as f:
        doc = BeautifulSoup(f, "html.parser")

        h1_element = doc.find('h1')
        if h1_element:
            text = h1_element.text.strip()
            parts = text.split()
            if len(parts) > 0:
                number = parts[0].replace(",", "")
                number = str(int(int(number) / 20) + 1) 
                print(number)
            else:
                print("Number not found")
        else:
            print("H1 element not found")

        print(number)
        os.remove("pagecount.html")
        return number
    
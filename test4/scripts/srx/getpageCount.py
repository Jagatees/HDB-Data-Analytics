from bs4 import BeautifulSoup
from selenium import webdriver
import os



def main():
    # Set the path to the Chrome WebDriver executable
    chrome_driver_path = '/Users/jagatees/Downloads/chromedriver'

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome()

    # Open the URL
    url = 'https://www.srx.com.sg/singapore-property-listings/hdb-for-sale?page=1'
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

        # Find the h1 element and extract the text
        h1_element = doc.find('h1')
        if h1_element:
            text = h1_element.text.strip()
            # Split the text to get the number part
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
    
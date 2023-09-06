from bs4 import BeautifulSoup
import requests

# web scrapping
def displayText():
    url = "https://www.newegg.com/global/sg-en/msi-geforce-rtx-3060-rtx-3060-ventus-3x-12g-oc/p/N82E16814137631"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    # print(doc.prettify)

    prices = doc.find_all(text="$")
    parent = prices[0].parent
    strong = parent.find("strong")
    print(strong.text)

displayText()
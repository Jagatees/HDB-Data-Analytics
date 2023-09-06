from bs4 import BeautifulSoup
import requests
import re

# web scrapping
def displayText():
    # url = "https://www.newegg.com/global/sg-en/msi-geforce-rtx-3060-rtx-3060-ventus-3x-12g-oc/p/N82E16814137631"
    # result = requests.get(url)
    # doc = BeautifulSoup(result.text, "html.parser")
    # # print(doc.prettify)

    # prices = doc.find_all(text="$")
    # parent = prices[0].parent
    # strong = parent.find("strong")
    # print(strong.text)

    # with open("./scripts/index.html", "r") as f:
    #     doc = BeautifulSoup(f, "html.parser")

    #     tag = doc.find_all(text=re.compile("\$.*"), limit=1)
    #     for x in tag:
    #         print(x.strip())

    url = "https://coninmarketcap.com"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

      

displayText()
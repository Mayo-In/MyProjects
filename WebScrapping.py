# This code demonstrates web scraping by sending HTTP requests to a webpage using the requests library and parsing the HTML content
# with BeautifulSoup to extract specific data. It showcases the use of both libraries for efficient web data extraction.
# Website Used for scrapping --> https://books.toscrape.com/

import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook

r = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(r.text, 'html5lib')

data= {"Book_Titles":[], "Book_Prices":[], "Availability_Status":[]}
prices = soup.select("p.price_color")
availability = soup.select("i.icon-ok")

for title in soup.find_all("a"):
    if title.has_attr("title"):
        data["Book_Titles"].append(title.get("title"))  #Get the book tiles

for price in prices:
    data["Book_Prices"].append(price.text)  #Get the prices

for avail in availability:
    data["Availability_Status"].append("In Stock")  #Get the availability status


df = pd.DataFrame.from_dict(data)
df.to_csv("BookStore_Data.csv", index = False)

df = pd.DataFrame.from_dict(data)
df.to_excel("BookStore_Data.xlsx", index = False)

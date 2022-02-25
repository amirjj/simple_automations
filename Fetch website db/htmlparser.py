import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

file = "D:\\code\code\\nezam_mohandesi\\output\\backup\\out_page1.html"

data = []
list_header = []


soup = BeautifulSoup(open(file),'html.parser')


# soup = BeautifulSoup(open(file),'html.parser')
header = soup.find_all("table")[1].find("tr")

for item in header:
    try:
        # print(item.get_text().encode("windows-1256").decode("utf-8"))
        list_header.append(item.get_text().encode("windows-1256").decode("utf-8"))
    except:
        continue


HTML_data = soup.find_all("table")[1].find_all("tr")[1:]


for element in HTML_data:
    try:
        sub_data = []
        for sub_element in element:
            sub_data.append(sub_element.get_text().encode("windows-1256").decode("utf-8"))
    except:
        continue
    data.append(sub_data)

print(data)

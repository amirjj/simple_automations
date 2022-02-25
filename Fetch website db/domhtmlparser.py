import os
import sys
import pandas as pd
from xml.dom import minidom
from pathlib import Path


path = Path("output\\newbackup")

columns = []
data = []
for p in path.rglob("*.html"):
    file = p
    page = open(file, "r").read()
    doc = minidom.parseString(page)
    tbl = doc.getElementsByTagName("table")[1]
    rows = tbl.getElementsByTagName("tr")
    
    if columns == []:
        header = rows[0]
        header_titles = header.getElementsByTagName("th")
        for title in header_titles:
            if title.firstChild is None:
                columns.append("")
            else:
                columns.append(title.firstChild.nodeValue.encode("cp1256").decode("utf-8").strip())

    for row in rows[1:-2]:
        tds = row.getElementsByTagName("td")
        sub_data = []
        for td in tds:
            if td.firstChild is None:
                sub_data.append("")
            else:
                sub_data.append(td.firstChild.nodeValue.encode("cp1256").decode("utf-8").strip())
        data.append(sub_data)

dataFrame = pd.DataFrame(data = data, columns = columns)
dataFrame.to_csv('output.csv', encoding = "utf8")
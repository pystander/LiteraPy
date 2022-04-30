#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

import requests
from bs4 import BeautifulSoup

# 漢語多功能字庫
CHAR = "測"
URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word=" + CHAR

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

arr = []

for tag in soup.find_all('tr', class_='greyTr'):
    for i in tag.text.split('\n'):
        i.replace('\n', '')

        if i != '':
            arr.append(i)

print(arr[1])
print(arr[3])
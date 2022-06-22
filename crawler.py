#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import requests
from bs4 import BeautifulSoup

# 漢語多功能字庫 Multi-function Chinese Character Database
URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word="

def define(char: str):
    search_URL = URL + char
    response = requests.get(search_URL)

    # Check status
    if response.status_code != requests.codes.ok:
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    definition = []

    for tag in soup.find_all('tr', class_='greyTr'):
        for i in tag.text.split('\n'):
            i.replace('\n', '')

            if i != '':
                definition.append(i)

    print(definition[1])
    print(definition[3])

#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
from litera import *

dict_path = 'dict/dict.txt'

def dmod(mode = 'r', data = ''):
    # Initialize
    if mode == 'i':
        with open(dict_path, 'w', encoding='utf-8') as f:
            f.write("")
            print("Dictionary cleared")
    # Read
    elif mode == 'r':
        with open(dict_path, 'r', encoding='utf-8') as f:
            return f.read()
    # Write / Append
    elif mode == 'w' or mode == 'a':
        with open(dict_path, mode, encoding='utf-8') as f:
            f.write(data + '\n')

def parser(dict_list: list, delimiter: str, new_delimiter: str):
    for i in range(len(dict_list)): 
        dmod('a', dict_list[i].replace(delimiter, new_delimiter))
        
    print("Dictionary file updated")

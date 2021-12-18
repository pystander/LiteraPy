#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
from litera import *

dict_path = 'dict/dict.txt'

def mod(mode = 'r', data = ''):
    if mode == 'i':
        with open(dict_path, 'w', encoding='utf-8') as f:
            f.write("")
            print("Dictionary cleared")
    elif mode == 'r':
        with open(dict_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif mode == 'w':
        with open(dict_path, 'w', encoding='utf-8') as f:
            f.write(line)
            print("Dictionary updated")
    elif mode == 'a':
        with open(dict_path, 'a', encoding='utf-8') as f:
            f.write(line)
            print("Dictionary appended")

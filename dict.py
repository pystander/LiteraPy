#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import time
import json

DICT_PATH = 'dict/dict.txt'

# Dictionary modifier
def dmod(mode: str='r', data: str=''):
    # Initialize
    if mode == 'i':
        with open(DICT_PATH, 'w', encoding='utf-8') as f:
            f.write("")
            print("Dictionary cleared")

    # Read
    elif mode == 'r':
        with open(DICT_PATH, 'r', encoding='utf-8') as f:
            return f.read()

    # Write
    elif mode == 'w':
        if data == "":
            print("Missing line to be added")
            return

        with open(DICT_PATH, 'w', encoding='utf-8') as f:
            f.write(data)
            print("Dictionary updated")

    # Append
    elif mode == 'a':
        if data == "":
            print("Missing line to be added")
            return

        with open(DICT_PATH, 'a', encoding='utf-8') as f:
            f.write('\n' + data)
            print("Dictionary updated")

def parser(dict_list: list, delimiter: str, new_delimiter: str='\t'):
    add_list = []
    t_start = time.time()

    with open(DICT_PATH, 'r', encoding='utf-8') as f:
        origin_list = f.readlines()

    for i in range(len(dict_list)):
        add_list.append(dict_list[i].replace(delimiter, new_delimiter))

    add_list = origin_list + add_list
    add_list.sort()

    with open(DICT_PATH, 'a', encoding='utf-8') as f:
        for line in add_list:
            f.write(line + '\n')

    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Dictionary file updated (" + str(interval) + " seconds)")

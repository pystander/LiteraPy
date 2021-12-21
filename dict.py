#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import time
from litera import *

dict_path = 'dict/dict.txt'

def dmod(mode: str='r', data: str=''):
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
            print("Dictionary updated")

def parser(dict_list: list, delimiter: str, new_delimiter: str='\t'):
    t_start = time.time()
    add_list = []
    
    for i in range(len(dict_list)):
        add_list.append(dict_list[i].replace(delimiter, new_delimiter))
        
    add_list.sort()
    
    with open(dict_path, 'a', encoding='utf-8') as f:
        for line in add_list:
            f.write(line + '\n')
            
    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Dictionary file updated (" + str(interval) + " seconds)")

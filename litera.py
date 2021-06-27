#!/usr/bin/env Python
# LiteraPy v1.0.3
# Copyright (c) 2021 pystander

# Import libraries
import re
import codecs
import gc
import time
import types
from pathlib import Path

# Read CEDICT file
if Path('cedict_ts.u8').is_file():
    ce_txt = open('cedict_ts.u8','r',encoding='utf-8')
    ce_line = [line.rstrip('\n') for line in ce_txt]
    ce_dict = list(ce_line)
    print("CEDICT loaded")
else:
    print("CEDICT file not found")

# Match-case will be introduced in Python 3.10
# menu() to be added

# Define functions
def fun():
    for f in globals().values():
        if type(f) == types.FunctionType:
            print(f)
            
def search():
    word = input("Search for related vocabularies:\n")
    size = len(word)
    matched = []
    t_start = time.time()
    
    for i in ce_line:
        start = i.find(' ') + 1
        
        # zh-CHT
        if i.startswith(word):
            matched.append(i[:start-1])
            
        # zh-CHS
        if word == i[start:start+size]:
            end = start + i[start:].find(' ')
            matched.append(i[start:end])
            
    result = list(dict.fromkeys(matched))
    count = len(result)
    
    if count > 0:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        
def pinyin():
    word = input("Search Pinyin for character(s):\n")
    char =[]
    matched = []
    t_start = time.time()
    
    # Split word into characters
    for i in word:
        char.append(i)
        
    # Perform Pinyin search per character
    for n in range(len(char)):
        ch = char[n]
        
        for i in ce_line:
            if i.startswith(ch + ' ') or ' ' + ch + ' ' in i:
                start = i.find('[') + 1
                end = i.find(']')
                if ch not in matched:
                    matched.append(i[start:end])
                    
    result = list(dict.fromkeys(matched))
    count = len(result)
    
    if count > 0:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

#!/usr/bin/env Python
# LiteraPy v1.0.2
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

# Define functions
def fun():
    for f in globals().values():
        if type(f) == types.FunctionType:
            print(f)

# Match-case will be introduced in Python 3.10 -> menu()
def search():
    word = input("Search for related vocabularies:\n")
    matched = []
    t_start = time.time()
    
    for i in ce_line:
        if word in i:
            start = i.find(word)
            end = i[start:].find(' ')
            matched.append(i[start:start+end])
            
    count = len(matched)
    if count > 0:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return matched
    else:
        print("No matched record")
        
def pinyin():
    word = input("Search for pinyin:\n")
    idx = [ce_line.index(i) for i in ce_line if i.startswith(word + " ")]
    pylist = []
    t_start = time.time()
    
    count = len(idx)
    if count > 0:
        for i in range(count):
            start = ce_line[idx[i]].find('[')
            end = ce_line[idx[i]].find(']')
            pylist.append(ce_line[idx[i]][start+1:end])

        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return pylist
    else:
        print("No matched record")
    

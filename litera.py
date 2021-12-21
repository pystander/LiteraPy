#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import re
import codecs
import time
import types

# Load dictionary
with open('dict/cidian_zhzh-kfcd-2021524.txt','r',encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

# Define functions
# Match-case will be introduced in Python 3.10 -> menu() to be added
def search(word: str, lang: str='zh-CHT'):
    # Empty input
    if word == "":
        return None
    
    size = len(word)
    matched = []
    t_start = time.time()
    
    # Cidian
    for i in cidian:
        start = i.find('\t') + 1
        
        # zh-CHT
        if lang == 'zh-CHT':
            if i.startswith(word):
                matched.append(i[:start-1])
        # zh-CHS
        elif lang == 'zh-CHS':
            if word == i[start:start+size]:
                end = start + i[start:].find('\t')
                matched.append(i[start:end])
                
    # Optimize results
    temp = list(filter(None, list(dict.fromkeys(matched))))
    result = sorted(temp, key=len)
    
    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        return None

def adsearch(word: str, lang: str='zh-CHT'):
    # Empty input
    if word == '':
        return None
    
    size = len(word)
    matched = []
    t_start = time.time()
    
    # Cidian
    for i in cidian:
        start = i.find('\t') + 1
        
        # zh-CHT
        if lang == 'zh-CHT':
            if word in i[:start]:
                matched.append(i[:start-1])  
        # zh-CHS
        elif lang == 'zh-CHS':
            end = i[start:].find('\t') + start
            if word in i[start:end]:
                matched.append(i[start:end])
                
    # Optimize results
    temp = list(filter(None, list(dict.fromkeys(matched))))
    result = sorted(temp, key=len)
    
    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

def pinyin(word: str):
    char =[]
    matched = []
    t_start = time.time()
    
    if word == "":
        return None
    
    # Search whole phrase in Cidian
    for i in cidian:
        start = i.find('\t') + 1
        end = i[start:].find('\t')
        
        if i.startswith(word + '\t') or word == i[start:start+end]:
            matched.append(i[start+end+1:])
            
    # Optimize results
    temp = list(filter(None, list(dict.fromkeys(matched))))
    result = sorted(temp, key=len)
    
    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

def fun():
    for f in globals().values():
        if type(f) == types.FunctionType:
            print(f)

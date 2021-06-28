#!/usr/bin/env Python
# LiteraPy v1.0.5
# Copyright (c) 2021 pystander

# Import libraries
import re
import codecs
import time
import types
from pathlib import Path

# Read CEDICT file
if Path('cedict_ts.u8').is_file():
    with open('cedict_ts.u8','r',encoding='utf-8') as f:
        cedict = [line.rstrip('\n') for line in f]
        print("CEDICT loaded")
else:
    print("CEDICT file not found")
    
# Read Cidian file
if Path('cidian_zhzh-kfcd-2021524.txt').is_file():
    with open('cidian_zhzh-kfcd-2021524.txt','r',encoding='utf-8') as f:
        cidian = [line.rstrip('\n') for line in f]
        print("Cidian loaded")
        
# Default variables
supported = ['zh-CHT','zh-CHS']

# Classes
class Setting:
    # Default language = ['zh-CHT']
    language = ['zh-CHT']
    
    def addlang():
        print("Supported language code: ")
        print(supported)
        
        code = input("Enter language code to be added: \n")
        
        if code in supported:
            if code == 'zh-CHT':
                if code not in Setting.language:
                    Setting.language.append(code)
                    print("Language changed to: ")
                    print(Setting.language)
                else:
                    print("Language existed")
                    
            elif code == 'zh-CHS':
                if code not in Setting.language:
                    Setting.language.append(code)
                    print("Language changed to: ")
                    print(Setting.language)
                else:
                    print("Language existed")
        else:
            print("Language not supported")

    def dellang():
        print("Current language setting: ")
        print(Setting.language)
        
        code = input("Enter language code to be hidden: \n")
        if code in Setting.language:
            Setting.language.remove(code)
            print("Language changed to: ")
            print(Setting.language)
        else:
            print("Language not found in setting")

# Define functions
# Match-case will be introduced in Python 3.10 -> menu() to be added
def fun():
    for f in globals().values():
        if type(f) == types.FunctionType:
            print(f)
            
def search():
    word = input("Search collocations for character(s): \n")
    size = len(word)
    matched = []
    t_start = time.time()
    
#    # CEDICT
#    for i in cedict:
#        start = i.find(' ') + 1
#        
#        # zh-CHT
#        if 'zh-CHT' in Setting.language:
#            if i.startswith(word):
#                matched.append(i[:start-1])
#                
#        # zh-CHS
#        if 'zh-CHS' in Setting.language:
#            if word == i[start:start+size]:
#                end = start + i[start:].find(' ')
#                matched.append(i[start:end])

    # Cidian
    for i in cidian:
        start = i.find('\t') + 1
        
        # zh-CHT
        if 'zh-CHT' in Setting.language:
            if i.startswith(word):
                matched.append(i[:start-1])
                
        # zh-CHS
        if 'zh-CHS' in Setting.language:
            if word == i[start:start+size]:
                end = start + i[start:].find('\t')
                matched.append(i[start:end])
                
    result = list(filter(None, list(dict.fromkeys(matched))))
    count = len(result)
    
    if count > 0:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        
def pinyin():
    word = input("Search Pinyin for character(s): \n")
    char =[]
    matched = []
    t_start = time.time()
    
    # Split word into characters
    for i in word:
        char.append(i)
        
    # Perform Pinyin search per character
    for n in range(len(char)):
        ch = char[n]
        
        for i in cedict:
            if i.startswith(ch + ' ') or ' ' + ch + ' ' in i:
                start = i.find('[') + 1
                end = i.find(']')
                if ch not in matched:
                    matched.append(i[start:end])
                    
    result = list(filter(None, list(dict.fromkeys(matched))))
    count = len(result)
    
    if count > 0:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(count) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        

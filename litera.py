#!/usr/bin/env Python
# LiteraPy v1.0.8
# Copyright (c) 2021 pystander

# Import libraries
import re
import codecs
import time
import types

# Load dictionaries
with open('dict/cedict_ts.u8','r',encoding='utf-8') as f:
    cedict = [line.rstrip('\n') for line in f]
    print("CEDICT loaded")
    
with open('dict/cidian_zhzh-kfcd-2021524.txt','r',encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")
    
with open('dict/bad-words.txt','r',encoding='utf-8') as f:
    badword = [line.rstrip('\n') for line in f]
    print("Bad words loaded")
    
with open('dict/filter.txt','r',encoding='utf-8') as f:
    filt = [line.rstrip('\n') for line in f]
    print("Filter loaded")
    
# Default settings
supported = ['zh-CHT','zh-CHS']

# Classes
class Setting:
    language = 'zh-CHT' # Default language as 'zh-CHT'

# Define functions
# Match-case will be introduced in Python 3.10 -> menu() to be added
def fun():
    for f in globals().values():
        if type(f) == types.FunctionType:
            print(f)

def lang():
    print("Current language: " + Setting.language)
    code = input("Enter preferred language code: " + str(supported) + "\n")
    
    if code == 'zh-CHT':
        Setting.language = 'zh-CHT'
        print("Language changed to: " + Setting.language)
        
    elif code == 'zh-CHS':
        Setting.language = 'zh-CHS'
        print("Language changed to: " + Setting.language)
        
    else:
        print("Language not supported")

def search():
    word = input("Search collocations for character(s): \n")
    size = len(word)
    matched = []
    t_start = time.time()
    
    # CEDICT
    for i in cedict:
        start = i.find(' ') + 1
        
        # zh-CHT
        if Setting.language == 'zh-CHT':
            if i.startswith(word) and not any(item in i for item in badword + filt):
                matched.append(i[:start-1])
                
        # zh-CHS
        if Setting.language == 'zh-CHS':
            if word == i[start:start+size] and not any(item in i for item in badword + filt):
                end = start + i[start:].find(' ')
                matched.append(i[start:end])
                
    # Cidian
    for i in cidian:
        start = i.find('\t') + 1
        
        # zh-CHT
        if Setting.language == 'zh-CHT':
            if i.startswith(word):
                matched.append(i[:start-1])
                
        # zh-CHS
        if Setting.language == 'zh-CHS':
            if word == i[start:start+size]:
                end = start + i[start:].find('\t')
                matched.append(i[start:end])
                
    # Optimize results
    result = sorted(list(filter(None, list(dict.fromkeys(matched)))),key=len)
    
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

def adsearch():
    word = input("Advanced search for character(s): \n")
    size = len(word)
    matched = []
    t_start = time.time()
    
    # CEDICT
    for i in cedict:
        start = i.find(' ') + 1
        
        # zh-CHT
        if Setting.language == 'zh-CHT':
           if word in i[:start] and not any(item in i for item in badword + filt):
                matched.append(i[:start-1])
                
        # zh-CHS
        if Setting.language == 'zh-CHS':
            end = i[start:].find(' ') + start
            if word in i[start:end] and not any(item in i for item in badword + filt):
                matched.append(i[start:end])
                
    # Cidian
    for i in cidian:
        start = i.find('\t') + 1
        
        # zh-CHT
        if Setting.language == 'zh-CHT':
            if word in i[:start]:
                matched.append(i[:start-1])
                
        # zh-CHS
        if Setting.language == 'zh-CHS':
            end = i[start:].find('\t') + start
            if word in i[start:end]:
                matched.append(i[start:end])
                
    # Optimize results
    result = sorted(list(filter(None, list(dict.fromkeys(matched)))),key=len)
    
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

def pinyin():
    word = input("Search Pinyin for character(s): \n")
    char =[]
    matched = []
    t_start = time.time()
    
    # Search whole phrase in Cidian
    for i in cidian:
        start = i.find('\t') + 1
        end = i[start:].find('\t')
        
        if i.startswith(word + '\t') or word == i[start:start+end]:
            matched.append(i[start+end+1:])
            
    # Search whole phrase in CEDICT
    if not matched:
        for i in cedict:
            start = i.find(' ') + 1
            end = i[start:].find(' ')
            
            if i.startswith(word + ' ') or word == i[start:start+end]:
                start = i.find('[') + 1
                end = i.find(']')
                matched.append(i[start:end].lower())
                
    # If no matched, search per character
    if not matched:
        for i in cedict:
            for ch in word:
                if i.startswith(ch + ' ') or ' ' + ch + ' ' == i[1:4]:
                    start = i.find('[') + 1
                    end = i.find(']')
                    matched.append(i[start:end].lower())
                    
    result = list(filter(None, list(dict.fromkeys(matched))))
    
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")

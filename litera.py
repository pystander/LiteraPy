#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import time
import json

DICT_PATH = 'dict/dict.txt'
IDX_PATH = 'dict/index.json'

# Load dictionary and index table
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

with open(IDX_PATH, 'r', encoding='utf-8') as f:
    idx_dict = json.load(f)
    print("Index table loaded")

# Define functions
def search(word: str, lang: str='zh-CHT', delimiter: str='\t'):
    # Empty input
    if not word:
        return None

    matched = []
    t_start = time.time()

    # Try search by index; else search all
    try:
        for key in idx_dict:
            if word in key:
                start, end = idx_dict[key]
                print("Index existed")
                break

        for line in cidian[start:end]:
            chunks = line.split(delimiter)

            # zh-CHT
            if lang == 'zh-CHT':
                matched.append(chunks[0])
            # zh-CHS
            elif lang == 'zh-CHS':
                matched.append(chunks[1])

    except:
        for line in cidian:
            chunks = line.split(delimiter)

            # zh-CHT
            if lang == 'zh-CHT':
                if chunks[0].startswith(word):
                    matched.append(chunks[0])
            # zh-CHS
            elif lang == 'zh-CHS':
                if chunks[1].startswith(word):
                    matched.append(chunks[1])

    # Optimize results
    result = sorted(matched, key=len)

    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        return None

def adsearch(word: str, lang: str='zh-CHT', delimiter: str='\t'):
    # Empty input
    if not word:
        return None

    matched = []
    t_start = time.time()

    # Cidian
    for line in cidian:
        chunks = line.split(delimiter)

        # zh-CHT
        if lang == 'zh-CHT':
            if word in chunks[0]:
                matched.append(chunks[0])
        # zh-CHS
        elif lang == 'zh-CHS':
            if word in chunks[1]:
                matched.append(chunks[1])

    # Optimize results
    result = sorted(matched, key=len)

    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Total of " + str(len(result)) + " record(s) (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        return None

def pinyin(word: str):
    if word == "":
        return None

    result = ""
    t_start = time.time()

    # Search whole phrase in Cidian
    for line in cidian:
        tap = line.find('\t') + 1
        tap2 = line[tap:].find('\t')

        if line.startswith(word + '\t') or word == line[tap:tap+tap2]:
            result = line[tap+tap2+1:]
            break

    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Record found (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        return None

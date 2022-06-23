#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import time
import json
from trie import Trie

DICT_PATH = 'dict/dict.txt'
IDX_PATH = 'dict/index.json'

# Load dictionary
try:
    with open(DICT_PATH, 'r', encoding='utf-8') as f:
        cidian = [line.rstrip('\n') for line in f]
        print("Cidian loaded")

except FileNotFoundError:
    print("Dictionary not found")
    exit(1)

# Build trie by dict
trie_cht = Trie().build_trie(lang='zh-CHT')
trie_chs = Trie().build_trie(lang='zh-CHS')

# Define functions
def search(word: str, lang: str='zh-CHT', delimiter: str='\t'):
    # Empty input
    if not word:
        return None

    matched = []
    t_start = time.time()

    # Try search by index; else search all
    try:
        if lang == 'zh-CHT':
            matched = trie_cht.prefix_search(word)
        elif lang == 'zh-CHS':
            matched = trie_chs.prefix_search(word)

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

def pinyin(word: str, delimiter: str='\t'):
    if word == "":
        return None

    result = ""
    t_start = time.time()

    # Search whole phrase in Cidian
    for line in cidian:
        chunks = line.split('\t')

        if chunks[0] == word or chunks[1] == word:
            result = chunks[2]

    # Output search results
    if result:
        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Record found (" + str(interval) + " seconds)")
        return result
    else:
        print("No matched record")
        return None

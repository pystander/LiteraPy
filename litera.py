#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import ast
import time

DICT_PATH = 'dict/dict.txt'
IDX_PATH = 'dict/index.txt'

# Load dictionary and index table
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

with open(IDX_PATH, 'r', encoding='utf-8') as f:
    idx_dict = ast.literal_eval(f.read())
    print("Index table loaded")

# Define functions
def search(word: str, lang: str='zh-CHT'):
    # Empty input
    if word == "":
        return None

    size = len(word)
    matched = []
    t_start = time.time()

    # Try search by index; else search all
    try:
        for key in idx_dict:
            if word in key:
                start, end = idx_dict[key]
                break

        for line in cidian[start:end]:
            tap = line.find('\t') + 1

            # zh-CHT
            if lang == 'zh-CHT':
                matched.append(line[:tap-1])
            # zh-CHS
            elif lang == 'zh-CHS':
                end = tap + line[tap:].find('\t')
                matched.append(line[tap:end])

    except:
        for line in cidian:
            tap = line.find('\t') + 1

            # zh-CHT
            if lang == 'zh-CHT':
                if line.startswith(word):
                    matched.append(line[:tap-1])
            # zh-CHS
            elif lang == 'zh-CHS':
                if word == line[tap:tap+size]:
                    end = tap + line[tap:].find('\t')
                    matched.append(line[tap:end])

    # Optimize results
    result = sorted(matched, key=len)

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

    matched = []
    t_start = time.time()

    # Cidian
    for line in cidian:
        tap = line.find('\t') + 1

        # zh-CHT
        if lang == 'zh-CHT':
            if word in line[:tap]:
                matched.append(line[:tap-1])
        # zh-CHS
        elif lang == 'zh-CHS':
            end = tap + line[tap:].find('\t')

            if word in line[tap:end]:
                matched.append(line[tap:end])

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
    matched = []
    t_start = time.time()

    if word == "":
        return None

    # Search whole phrase in Cidian
    for line in cidian:
        start = line.find('\t') + 1
        end = line[start:].find('\t')

        if line.startswith(word + '\t') or word == line[start:start+end]:
            matched.append(line[start+end+1:])

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

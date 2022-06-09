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
    print("Search index loaded")

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

    # Write / Append
    elif mode == 'w' or mode == 'a':
        if data == "":
            print("Missing line to be added")
            return None

        with open(DICT_PATH, mode, encoding='utf-8') as f:
            f.write(data + '\n')
            print("Dictionary updated")

def parser(dict_list: list, delimiter: str, new_delimiter: str='\t'):
    t_start = time.time()
    add_list = []

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

def idx(word_CHT: str, word_CHS: str):
    start = end = 0

    # Start index
    for i, line in enumerate(cidian):
        tap = line.find('\t') + 1

        if line.startswith(word_CHT) and line[tap:].startswith(word_CHS):
            start = i
            break

    # End index
    for i, line in enumerate(cidian[start:]):
        tap = line.find('\t') + 1

        if not line.startswith(word_CHT) or not line[tap:].startswith(word_CHS):
            end = start + i
            break

    return start, end

def idx_update():
    idx_dict = {}

    for line in cidian:
        if line:
            tap = line.find('\t') + 1
            key_CHT, key_CHS = line[0], line[tap]

            if (key_CHT, key_CHS) not in idx_dict:
                idx_dict[(key_CHT, key_CHS)] = idx(key_CHT, key_CHS)

    with open(IDX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(idx_dict))
        print("Index table updated")

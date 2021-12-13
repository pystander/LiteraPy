#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import sys
import re
import time
import jieba
import json
import itertools
import ast
from litera import search
from collections import Counter

# Load jieba settings
jieba.set_dictionary('dict/dict.txt')

# Define functions
def analyse(fq_mode=True, check_dict=False):
    txt = input("Enter the whole paragraph / sentence(s): \n")
    
    if txt == "":
        return None
    
    clauses = list(filter(None,re.split('。|，|；|：|、|？|！|「|」|“ |”|（|）|《|》|——|……',txt)))
    temp = []
    result = []
    t_start = time.time()
    
    # Cut by jieba
    for clause in clauses:
        seg_list = jieba.lcut(clause, cut_all=True)
        temp.append(' '.join(seg_list))
        
    # Split into phrases
    for i in temp:
        result.append(i.split(' '))
        
    # Match dictionary words
    if check_dict:
        result = checklist(list(itertools.chain(*result)))
    else:
        result = list(itertools.chain(*result))
        
    # Word frequency count
    if fq_mode:
        with open('dict/frequency.json', 'r', encoding='utf-8') as fr:
            fq = json.load(fr)
            fq_dict = dict(Counter(result) + Counter(fq))
            
        with open('dict/frequency.json','w', encoding='utf-8') as fw:
            json.dump(fq_dict, fw, ensure_ascii=False, sort_keys=True, indent=4)
            
    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Time interval: " + str(interval) + " seconds")
    return result

def checklist(clauses: list):
    cklist = []
    
    # Check if phrase in dict
    for i in clauses:
        if search(i):
            cklist.append(i)
            
    return cklist

def fq():
    with open('dict/frequency.json','r',encoding='utf-8') as fr:
        fq = json.load(fr)
        return fq

def initfq():
    with open('dict/frequency.json', 'w', encoding='utf-8') as fw:
        json.dump({}, fw)
        print("Frequency file cleared")

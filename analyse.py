#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import re
import time
import jieba
import itertools
import ast
from litera import search
from collections import Counter

# Load jieba settings
jieba.enable_paddle()
jieba.set_dictionary('dict/dict.txt')

# Define functions
def analyse(fq_mode=False, check_dict=False):
    txt = input("Enter the whole paragraph / sentence(s): \n")
    
    if txt == "":
        return None
    
    clauses = list(filter(None,re.split('。|，|；|：|、|？|！|「|」|“ |”|（|）',txt)))
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
        
    if check_dict:
        result = checklist(list(itertools.chain(*result)))
    else:
        result = list(itertools.chain(*result))
        
    result_fq = dict(Counter(result))
    
    # Word frequency count
    if fq_mode:
        with open('dict/frequency.txt',encoding='utf-8') as f:
            fq = ast.literal_eval(f.read())
            learnt = dict(Counter(fq) + Counter(result_fq))
            
            with open('dict/frequency.txt','r+',encoding='utf-8') as f:
                f.write(str(learnt))
                
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
    with open('dict/frequency.txt','r',encoding='utf-8') as f:
        fq = ast.literal_eval(f.read())
        return fq

def initfq():
    with open('dict/frequency.txt','r+',encoding='utf-8') as f:
        data = f.read()
        f.seek(0)
        f.write('{}')
        f.truncate()
        print("Frequency file cleared")

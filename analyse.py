#!/usr/bin/env Python
# LiteraPy v1.0.8
# Copyright (c) 2021 pystander

# Import libraries
import re
import time
import jieba # Package 'jieba' required
import itertools
import ast
from collections import Counter

# Load jieba settings
jieba.enable_paddle()
jieba.set_dictionary('dict/dict.txt')

# Define functions
def analyse():
    txt = input("Enter the whole paragraph / sentence(s): \n")
    clauses = list(filter(None,re.split('。|，|；|：|、|？|！|「|」|“ |”',txt)))
    temp = []
    result = []
    t_start = time.time()
    
    # Cut by jieba
    for clause in clauses:
        seg_list = jieba.lcut(clause,use_paddle=True)
        temp.append(' '.join(seg_list))
        
    # Split into phrases
    for i in temp:
        result.append(i.split(' '))
        
    result = list(itertools.chain(*result))
    result_fq = dict(Counter(result))
    
    # Read and store frequency
    with open('dict/frequency.txt',encoding='utf-8') as f:
        fq = ast.literal_eval(f.read())
        learnt = dict(Counter(fq) + Counter(result_fq))
        
        with open('dict/frequency.txt','r+',encoding='utf-8') as f:
            f.write(str(learnt))
            
    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Time interval: " + str(interval) + " seconds")
    return result
    
def initfq():
    with open('dict/frequency.txt','r+',encoding='utf-8') as f:
        data = f.read()
        f.seek(0)
        f.write('{}')
        f.truncate()
        print("Frequency file cleared")
        
def fq():
    with open('dict/frequency.txt','r',encoding='utf-8') as f:
        fq = ast.literal_eval(f.read())
        return fq

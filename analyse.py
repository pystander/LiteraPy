#!/usr/bin/env python3
# LiteraPy v1.0.9
# Copyright (c) 2021 pystander

# Import libraries
import re
import time
import jieba # Package 'jieba' required
import itertools
import ast
from collections import Counter
from litera import search

# Load jieba settings
jieba.enable_paddle()
jieba.set_dictionary('dict/dict.txt')

# Default settings
class Setting:
    fq_mode = True

# Define functions
def analyse():
    txt = input("Enter the whole paragraph / sentence(s): \n")
    clauses = list(filter(None,re.split('。|，|；|：|、|？|！|「|」|“ |”|（|）',txt)))
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
        
    result = checklist(list(itertools.chain(*result)))
    result_fq = dict(Counter(result))
    
    # Word frequency count
    if Setting.fq_mode:
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
    
    for i in clauses:
        if search(i):
            cklist.append(i)
            
    remain = list(set(clauses) - set(cklist))
    cklist.extend(remain)
    
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

def fqmode():
    print("Current FQ mode: " + str(Setting.fq_mode))
    code = input("Enter preferred mode: ['True', 'False']\n")
    
    if code == "True":
        Setting.fq_mode = True
        print("FQ mode changed to: " + str(Setting.fq_mode))
        
    elif code == "False":
        Setting.fq_mode = False
        print("FQ mode changed to: " + str(Setting.fq_mode))
        
    else:
        print("FQ mode not supported")

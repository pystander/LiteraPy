#!/usr/bin/env Python

# Import libraries
import re
import time
import jieba # Package 'jieba' required
import jieba.posseg as pseg
import itertools
import json
from collections import Counter

# Enable jieba paddle mode
jieba.enable_paddle()

# Define functions
def analyse():
    txt = input("Enter the whole paragraph / sentence(s): \n")
    clauses = list(filter(None,re.split('。|，|；|：|、|？|！|「|」|“ |”',txt)))
    temp = []
    result = []
    t_start = time.time()
    
    for clause in clauses:
        seg_list = jieba.lcut(clause,use_paddle=True)
        temp.append(' '.join(seg_list))
        
    for i in temp:
        result.append(i.split(' '))
        
    result = list(itertools.chain(*result))
    result_count = dict(Counter(result))
#    learn(result_count)
    
    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Time interval: " + str(interval) + " seconds")
    
    print(result)
    print(result_count)
    
#def learn(result_count: dict):
#    with open('dict/count.json','a+') as outfile:
#        ob = json.load(outfile)
#        
#        learnt = dict(Counter(ob) + Counter(result_count))
#        json.dumps(learnt,outfile)

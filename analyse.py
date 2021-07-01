#!/usr/bin/env Python

# Import libraries
import re
import time
import jieba # Package 'jieba' required

def analyse():
    txt = input("Enter the whole paragraph / sentence(s): \n")
    clauses = list(filter(None,re.split('。|，|；|：|？|！|「|」|“ |”',txt)))
    t_start = time.time()
    
    for clause in clauses:
        seg_list = jieba.lcut(clause)
        print('/'.join(seg_list))
        
    interval = '{0:.3f}'.format(time.time() - t_start)
    print("Time interval: " + str(interval) + " seconds")

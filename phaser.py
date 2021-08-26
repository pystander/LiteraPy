#!/usr/bin/env python3
# LiteraPy v1.0.8
# Copyright (c) 2021 pystander

# Import libraries
import re
import codecs
import time
import types

# Load dictionaries
with open('dict/cedict_ts.u8','r',encoding='utf-8') as f:
    cedict = [line.rstrip('\n') for line in f]
    print("CEDICT loaded")
    
# Formating
phaser = []

for i in cedict:
    start = i.find(' ') + 1
    end = start + i[start:].find(' ')
    vocab = i[:end].split(' ')
    
    start = i.find('[') + 1
    end = i.find(']')
    pinyin = [i[start:end]]
    
    start = i.find('/') + 1
    end = start + i[start:].find('/')
    meaning = [i[start:end]]
    
    phaser.append(vocab + pinyin + meaning)
    

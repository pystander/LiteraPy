#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import json

def init_dict():
    with open('dict/dict.json', 'r', encoding='utf-8') as f:
        json.dump({}, f)
        print("Dictionary cleared")

def read():
    with open('dict/dict.json', 'r', encoding='utf-8') as f:
        rdict = json.load(f)
        return rdict

#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import collections

DICT_PATH = 'dict/dict.txt'

# Load dictionary
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

# Node
class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.char = ""
        self.is_word = False

# Trie
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        cur = self.root

        for char in word:
            if char not in cur.child:
                cur.child[char] = Node()

            cur = cur.child[char]

        cur.char = word
        cur.is_word = True

    def search(self, word):
        cur = self.root

        for char in word:
            if char not in cur.child:
                return False
            else:
                cur = cur.child[char]

        return cur.char

    def start_wtih(self, prefix):
        cur = self.root

        for char in prefix:
            if char not in cur.child:
                return False
            else:
                cur = cur.child[char]

        return True

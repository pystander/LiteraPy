#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import pygtrie

DICT_PATH = 'dict/dict.txt'

# Load dictionary
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

# Node
class Node:
    def __init__(self):
        self.child = {Node}
        self.is_word = False

# Trie
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for char in word:
            cur = cur.child[char]

        cur.is_word = True

    def search(self, word):
        cur = self.root

        for char in word:
            cur = cur.child.get(char)

            if not cur:
                return False

        return True

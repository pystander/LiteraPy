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
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False

# Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()

        node.is_word = True

    def search(self, word):
        node = self.root

        for char in word:
            node = node.child.get(char)

            if not node:
                return False

        return node.is_word

    def start_wtih(self, prefix):
        node = self.root

        for char in prefix:
            node = node.child.get(char)

            if not node:
                return False

        return True

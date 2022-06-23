#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import collections
import time

DICT_PATH = 'dict/dict.txt'

# Load dictionary
with open(DICT_PATH, 'r', encoding='utf-8') as f:
    cidian = [line.rstrip('\n') for line in f]
    print("Cidian loaded")

# Node
class TrieNode:
    def __init__(self, char: str):
        self.child = collections.defaultdict(TrieNode)
        self.char = char
        self.is_end = False

# Trie
class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                new_node = TrieNode(char)
                node.child[char] = new_node
                node = new_node

        node.is_end = True

    def search(self, word: str):
        node = self.root

        for char in word:
            node = node.child.get(char)

            if not node:
                return False

        return node.is_end

    def start_wtih(self, prefix: str):
        node = self.root

        for char in prefix:
            node = node.child[char]

            if not node:
                return False

        return True

    def prefix_search(self, prefix: str):
        node = self.root

        for char in prefix:
            if char in node.child:
                node = node.child[char]
            else:
                return []

        self.result = []
        self.dfs(node, prefix[:-1])

        return self.result

    def dfs(self, node: TrieNode, prefix: str):
        if node.is_end:
            self.result.append((prefix + node.char))

        for child in node.child.values():
            self.dfs(child, prefix + node.char)

    # Build trie by dict
    def build_trie(self, dict_list: list=cidian, delimiter: str='\t'):
        t_start = time.time()

        for line in dict_list:
            chunks = line.split(delimiter)
            self.insert(chunks[0])
            self.insert(chunks[1])

        interval = '{0:.3f}'.format(time.time() - t_start)
        print("Trie updated (" + str(interval) + " seconds)")

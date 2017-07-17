from collections import defaultdict


class Trie:

    def __init__(self):
        self.trie = defaultdict(lambda: {})

    def insert(self, string):
        node = self.trie
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]


if __name__ == '__main__':
    trie = Trie()
    trie.insert('skittles')
    trie.insert('chocolate')
    trie.insert('skipper')

    print(trie.trie)

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

    def get_all_with_prefix(self, prefix):
        node = self.trie
        for char in prefix:
            node = node[char]
        words = []
        for char in node:
            suffix = self._get_suffix(char, node)
            words.append( prefix + suffix )
        return words

    def _get_suffix(self, char, node, word=None):
        if not word:
            word = []
        if not node[char]:
            return ''.join(word) + char
        word.append(char)
        for next_char in node[char]:
            return self._get_suffix(char=next_char, node=node[char], word=word)

if __name__ == '__main__':
    trie = Trie()

    trie.insert('skittles')
    print(f">>> trie.insert('skittles')")

    trie.insert('chocolate')
    print(f">>> trie.insert('chocolate')")

    trie.insert('chester')
    print(f">>> trie.insert('chester')")

    trie.insert('skipper')
    print(f">>> trie.insert('skipper')")

    print(f">>> Trie: \n\n{trie.trie}")

    print(f"\n>>> trie.get_all_with_prefix('ski')")
    print(f"{trie.get_all_with_prefix('ski')})")

    print(f"\n>>> trie.get_all_with_prefix('ch')")
    print(f"{trie.get_all_with_prefix('ch')})")

import sys

class PrefixFinder:
    def __init__(self):
        self.trie_map = {"": ("", [], False)}  # map from prefix to children, and whether this prefix is the terminal of a word

    def attempt_add(self, word):
        current_node = self.trie_map[""]  # root
        for idx,letter in enumerate(word):
            next_prefix = word[0:idx+1]
            next_node = self.trie_map.get(next_prefix)
            if not next_node:
                next_node = (next_prefix, [], idx == len(word) - 1)
                self.trie_map[next_node[0]] = next_node
                current_node[1].append(next_node[0])
            elif next_node[2] or idx == len(word) - 1:
                print "BAD SET\n{}".format(word)
                return word
            current_node = next_node

finder = PrefixFinder()
def solve():
    for word in list(sys.stdin)[1:]:
        if finder.attempt_add(word.strip()):
            return
    print "GOOD SET"

solve()
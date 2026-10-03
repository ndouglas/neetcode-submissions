class PrefixTreeNode:
    
    def __init__(self):
        self.children = {}
        self.word = False

    def search(self, word: str) -> bool:
        length = len(word)
        if length == 0:
            return self.word
        elif length == 1:
            if word == '.':
                for k, c in self.children.items():
                    if c.word:
                        return True
            elif word in self.children:
                return self.children[word].word
        elif word[0] == '.':
            for k, c in self.children.items():
                if c.search(word[1:]):
                    return True
        elif word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False

class WordDictionary:

    def __init__(self):
        self.root = PrefixTreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixTreeNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        return self.root.search(word)

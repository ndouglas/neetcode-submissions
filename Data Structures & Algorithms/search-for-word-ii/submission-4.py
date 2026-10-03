def getIndex(c):
    return ord(c) - ord('a')

class PrefixTreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word: str, idx: int):
        curr = self
        curr.refs += 1
        for char in word:
            index = getIndex(char)
            if not curr.children[index]:
                curr.children[index] = PrefixTreeNode()
            curr = curr.children[index]
            curr.refs += 1
        curr.idx = idx

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = PrefixTreeNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])

        result = []

        def dfs(row: int, col: int, node: PrefixTreeNode) -> int:
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] == '*' or not node.children[getIndex(board[row][col])]:
                return 0
            tmp = board[row][col]
            board[row][col] = '*'
            prev = node
            node = node.children[getIndex(tmp)]
            found = 0
            if node.idx != -1:
                result.append(words[node.idx])
                node.idx = -1
                found += 1
            found += dfs(row + 1, col, node)
            found += dfs(row - 1, col, node)
            found += dfs(row, col + 1, node)
            found += dfs(row, col - 1, node)
            board[row][col] = tmp
            node.refs -= found
            if not node.refs:
                prev.children[getIndex(tmp)] = None
            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                root.refs -= dfs(row, col, root)
            
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append([root])
        res = []
        while queue:
            nodes = queue.popleft()
            row = []
            if not nodes:
                break
            for i in range(len(nodes)):
                node = nodes[i]
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)
            if row:
                queue.append(row)
            last = nodes[-1]
            res.append(last.val)
        return res
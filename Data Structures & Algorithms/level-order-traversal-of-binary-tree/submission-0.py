# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root:
            queue.append([root])
        while queue:
            nodes = queue.popleft()
            if not nodes:
                break
            res.append([ node.val for node in nodes])
            q_next = []
            for i in range(len(nodes)):
                n = nodes[i]
                if n.left:
                    q_next.append(n.left)
                if n.right:
                    q_next.append(n.right)
            queue.append(q_next)
        return res        
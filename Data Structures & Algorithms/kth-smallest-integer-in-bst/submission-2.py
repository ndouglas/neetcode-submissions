# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root: TreeNode, c: int) -> (int, int):
            if root.left:
                (new_c, val) = traverse(root.left, c)
                if new_c == k:
                    return (new_c, val)
                else:
                    c = new_c
            c += 1
            if c == k or not root.right:
                return (c, root.val)
            if root.right:
                (new_c, val) = traverse(root.right, c)
                return (new_c, val)
            
        return traverse(root, 0)[1]
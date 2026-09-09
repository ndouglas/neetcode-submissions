# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverseAndInsert(root: Optional[TreeNode], val: int):
            if not root:
                return
            if val < root.val:
                if root.left:
                    traverseAndInsert(root.left, val)
                else:
                    root.left = TreeNode(val, None, None)
            else:
                if root.right:
                    traverseAndInsert(root.right, val)
                else:
                    root.right = TreeNode(val, None, None)
        if not root:
            root = TreeNode(val, None, None)
            return root
        traverseAndInsert(root, val)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        visited = []
        result = []
        if root:
            stack.append(root)
            visited.append(False)
        while stack:
            node = stack.pop()
            node_visited = visited.pop()
            if node_visited:
                result.append(node.val)
            else:
                stack.append(node)
                visited.append(True)
                if node.right:
                    stack.append(node.right)
                    visited.append(False)
                if node.left:
                    stack.append(node.left)
                    visited.append(False)

        return result
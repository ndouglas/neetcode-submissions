# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def insertNode(root: TreeNode, node: TreeNode):
            if node.val < root.val:
                if root.left:
                    insertNode(root.left, node)
                else:
                    root.left = node
            elif node.val > root.val:
                if root.right:
                    insertNode(root.right, node)
                else:
                    root.right = node
        def deleteNodeLeft(root: TreeNode, left: TreeNode):
            left_left = left.left
            left_right = left.right
            if left_left:
                if left_right:
                    insertNode(left_left, left_right)
                root.left = left_left
            else:
                root.left = left_right
        def deleteNodeRight(root: TreeNode, right: TreeNode):
            right_left = right.left
            right_right = right.right
            if right_left:
                if right_right:
                    insertNode(right_left, right_right)
                root.right = right_left
            else:
                root.right = right_right
        def findNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return None
            elif key == root.val:
                return root
            elif key < root.val:
                if findNode(root.left, key):
                    deleteNodeLeft(root, root.left)
            elif findNode(root.right, key):
                deleteNodeRight(root, root.right)
        if root.val == key:
            left = root.left
            right = root.right
            if left and right:
                insertNode(left, right)
                return left
            elif left:
                return left
            elif right:
                return right
            else:
                return None
        else:
            findNode(root, key)
            return root

        
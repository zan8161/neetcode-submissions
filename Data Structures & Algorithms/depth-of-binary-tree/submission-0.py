# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        stack = []
        nextlevel_stack = [root]
        while nextlevel_stack:
            stack = nextlevel_stack.copy()
            nextlevel_stack.clear()
            max_depth += 1
            while stack:
                node = stack.pop()
                if node.left is not None:
                    nextlevel_stack.append(node.left)
                if node.right is not None:
                    nextlevel_stack.append(node.right)
        return max_depth
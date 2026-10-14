# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root
            
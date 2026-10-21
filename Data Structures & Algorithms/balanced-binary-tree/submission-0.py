# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [root]
        h = {None: 0}

        while stack:
            node = stack[-1]
            if node.left and node.left not in h:
                stack.append(node.left)
            elif node.right and node.right not in h:
                stack.append(node.right)
            else:
                node = stack.pop()
                height = 1 + max(h[node.left], h[node.right])
                diff = abs(h[node.left] - h[node.right])
                
                if diff > 1:
                    return False

                h[node] = height
        return True
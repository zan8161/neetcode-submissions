# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        depth = {None: (0, 0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in depth:
                stack.append(node.left)
            elif node.right and node.right not in depth:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = depth[node.left]
                rightHeight, rightDiameter = depth[node.right]

                depth[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        return depth[root][1]
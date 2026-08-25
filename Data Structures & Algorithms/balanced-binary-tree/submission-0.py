# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def helper(node):
            if not node:
                return 0
            
            left= helper(node.left)
            right= helper(node.right)

            if abs(left-right) > 1:
                nonlocal res
                res = False
            
            return max(right, left) + 1
        
        helper(root)
        return res


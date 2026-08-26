# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        def helper(node):
            nonlocal res
            nonlocal k
            if not node:
                return
            left = helper(node.left)
            k-=1
            if k == 0:
                res = node.val
            right = helper(node.right)
        
        helper(root)
        return res
        
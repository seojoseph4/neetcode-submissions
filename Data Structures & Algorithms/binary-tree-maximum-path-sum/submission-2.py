# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        overallMax = float('-inf')

        def dfs(root):
            nonlocal overallMax
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right =  dfs(root.right)
            currMax = max(left+right+root.val, root.val+left, root.val+right, root.val)
            overallMax = max(currMax, overallMax)
            return max(root.val+left, root.val+right, root.val)

        dfs(root)
        return overallMax

        
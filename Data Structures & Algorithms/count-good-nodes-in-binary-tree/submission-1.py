# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node, runningmax):
            if not node:
                return 0
            runningmax = max(node.val, runningmax)

            
            if node.val >= runningmax:
                res = 1
            else:
                res = 0
            
            return res + helper(node.left, runningmax)  + helper(node.right, runningmax)

        return helper(root, float("-inf"))
            
        
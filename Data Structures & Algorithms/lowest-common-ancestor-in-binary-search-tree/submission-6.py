# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = None

        def helper(node):
            if not node:
                return None
            # if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
            #     return node
            elif node.val < p.val and node.val < q.val:
                return helper(node.right)
            
            if node.val > p.val and node.val > q.val:
                return helper(node.left)
            
            return node
        
        return helper(root)
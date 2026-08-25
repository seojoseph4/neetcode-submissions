# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        def helper(p):
            if not p:
                return False
            if p.val == subRoot.val:
                if same(p, subRoot):
                    return True
            return helper(p.left) or helper(p.right)
            
        def same(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val != q.val:
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)

        return helper(root)            
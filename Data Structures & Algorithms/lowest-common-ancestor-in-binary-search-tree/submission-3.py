# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val <  p.val and root.val < q.val:
            if root.right:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
        if root.val > p.val and root.val > q.val:
            if root.left:
                return self.lowestCommonAncestor(root.left, p,q)
            else:
                return root
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

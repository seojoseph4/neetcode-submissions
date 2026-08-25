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
                return False, False
            
            pleft, qleft = helper(node.left)
            pright, qright = helper(node.right)

            pstatus = (pleft or pright or node == p)
            qstatus = (qleft or qright or node == q)
            # print(node.val, pstatus, qstatus)
            nonlocal res
            if pstatus and qstatus and not res:
                res = node

            return pstatus, qstatus

        helper(root)
        return res
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for i in range(len(inorder)):
            hm[inorder[i]] = i
        
        g = 0
        def helper(l,r):
            nonlocal g
            if l > r:
                return None
            find = hm[preorder[g]]
            value = preorder[g]
            g+=1

            left = helper(l, find-1)
            right = helper(find+1,r)

            return TreeNode(value, left, right)
        
        return helper(0,len(inorder)-1)
            
            
            
        
        
        
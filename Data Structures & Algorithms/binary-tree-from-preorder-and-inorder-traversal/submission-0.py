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
        def helper(prestart, preend, instart, inend):
            if (prestart > preend) or (instart > inend):
                return None
            root = TreeNode(preorder[prestart])
            mid = hm[root.val]

            root.left = helper(prestart+1, prestart+mid-instart, instart, mid-1)
            root.right = helper(prestart + mid-instart + 1, preend, mid + 1, inend)
            return root

        return helper(0, len(preorder)-1,0, len(inorder)-1)


            
            
        
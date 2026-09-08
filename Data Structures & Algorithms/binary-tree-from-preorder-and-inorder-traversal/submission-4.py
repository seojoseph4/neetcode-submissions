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
        i = 0
        def helper(l,r):
            nonlocal i
            if i >= len(preorder):
                return None
            if l > r:
                return None
            curr = preorder[i]
            inorderi = hm[curr]
            i+=1
            left = helper(l,inorderi-1)
            right = helper(inorderi+1,r)

            return TreeNode(curr, left, right)

        return helper(0,len(preorder))

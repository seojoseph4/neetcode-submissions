# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for i, val in enumerate(inorder):
            hm[val] = i
        i = 0
        def helper(left, right):
            if left > right:
                return None
            nonlocal i
            
            element = preorder[i]
            i+=1
            m = hm[element]

            leftcall = helper(left, m-1)
            rightcall = helper(m+1, right)
            return TreeNode(element, leftcall, rightcall)

        return helper(0, len(inorder)-1)


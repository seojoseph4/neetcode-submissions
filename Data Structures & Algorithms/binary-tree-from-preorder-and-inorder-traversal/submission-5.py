# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = defaultdict(int)
        for i in range(len(inorder)):
            hm[inorder[i]] = i

        i = 0        
        def helper(l,r):
            nonlocal i
            if l > r or i >= len(preorder):
                return None
            find = hm[preorder[i]]
            curr = TreeNode(preorder[i])
            i+=1
            left = helper(l, find-1)
            right = helper(find+1, r)
            curr.left = left
            curr.right = right

            return curr
        
        return helper(0, len(preorder))


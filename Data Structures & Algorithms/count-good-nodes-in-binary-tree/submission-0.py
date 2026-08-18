# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        # res+=1
        res+=self.traverse(root, root.val)
        return res

    def traverse(self, curr: TreeNode, big: int):
        if not curr:
            return 0
        big = max(big, curr.val)
        left = 0
        right = 0
        if curr.left:
            left = self.traverse(curr.left, big)
        if curr.right:
            right = self.traverse(curr.right, big) 
        if curr.val < big:
            return left+right
        else:
            return 1+left+right



        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        
        q.append(root)
        while q:
            curr = []
            for _ in range(len(q)):
                element = q[0]
                q.popleft()
                curr.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            res.append(curr)
        
        return res
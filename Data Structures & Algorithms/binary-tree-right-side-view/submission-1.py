# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        res = []
        if not root:
            return res
        
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                if q[0]:
                    level.append(q[0])
                    q.append(q[0].left)
                    q.append(q[0].right)
                q.popleft()
            if level:
                res.append(level[-1].val)
        
        return res
        
        
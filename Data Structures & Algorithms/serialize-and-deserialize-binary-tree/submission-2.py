# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(curr):
            nonlocal res
            if not curr:
                res.append(".")
                return
            res.append(str(curr.val))
            left = dfs(curr.left)
            right = dfs(curr.right)
            
        dfs(root)
        # print(",".join(res))
        return ",".join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = data.split(",")
        i = 0
        print(l)
        def dfs():
            nonlocal i
            if l[i] == ".":
                i+=1
                return None
            
            curr = TreeNode(int(l[i]))
            # print(curr.val)
            i+=1
            curr.left = dfs()
            curr.right = dfs()
            return curr
        
        return dfs()

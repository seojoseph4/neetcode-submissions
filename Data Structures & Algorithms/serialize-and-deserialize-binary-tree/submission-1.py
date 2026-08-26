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

        def helper(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        # print(",".join(res))
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        i = 0
        def helper():
            nonlocal i
            if i >= len(arr) or arr[i] == "N":
                i+=1
                return None
            else:
                curr = TreeNode(int(arr[i]))
                i+=1
                left = helper()
                right = helper()
                curr.left = left
                curr.right = right
                return curr
        return helper()

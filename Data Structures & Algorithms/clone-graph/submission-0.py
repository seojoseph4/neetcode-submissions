"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}
        

        def dfs(curr):
            if curr in mapping:
                return mapping[curr]
            newnode = Node(curr.val)
            mapping[curr] = newnode
            for n in curr.neighbors:
                newnode.neighbors.append(dfs(n))
            return newnode

        return dfs(node)


            
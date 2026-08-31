"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(curr):
            if curr in seen:
                return seen[curr]
            dcopy = Node(curr.val)
            seen[curr] = dcopy
            for nei in curr.neighbors:
                dcopy.neighbors.append(dfs(nei))
            return dcopy

        return dfs(node) if node else None

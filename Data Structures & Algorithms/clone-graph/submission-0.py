"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # No node
        if not node:
            return None

        # Initiate a old to new hashmap
        oldToNew = {}

        # dfs
        def dfs(node):
            # If the new node appears in the hashmap, return the hashmap
            if node in oldToNew:
                return oldToNew[node]

            # Copy the node
            copy = Node(node.val)
            # Add copy to hashmap
            oldToNew[node] = copy

            # for node neighbours, append them in the copy neighbours
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        #Return
        return dfs(node)
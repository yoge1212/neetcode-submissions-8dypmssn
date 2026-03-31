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
        
        old_to_new = {}

        
        def dfs(current_node):
            new = Node(current_node.val, None)
            neighbors = current_node.neighbors
            new_neighbors = []
            old_to_new[current_node] = new
        
            for node in neighbors:
                if node in old_to_new:
                    new_neighbors.append(old_to_new[node])
                else:
                    new_neighbors.append(dfs(node))
            
            new.neighbors = new_neighbors
            return new

        return dfs(node)
        
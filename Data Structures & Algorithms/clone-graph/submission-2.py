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
        visited = set()
        graph = {}

        def dfs(node: Optional['Node']):
            if not node or node.val in graph:
                return

            graph[node.val] = Node(node.val)
            
            for neighbor in node.neighbors:
                if not neighbor.val in visited:
                    visited.add(neighbor.val)
                    dfs(neighbor)
                graph[node.val].neighbors.append(graph[neighbor.val])

        dfs(node)
        return graph[node.val]

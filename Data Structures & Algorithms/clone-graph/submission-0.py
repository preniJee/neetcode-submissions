"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # if not node.neighbors:
        #     print("here")
        #     return "[[]]"

        adj_dict = {}
        adj_dict[node] = Node(node.val)
        visited = set()
        q = deque()
        q.append(node)
        visited.add(node)

        while q: 
            curr = q.pop()
            # adj_dict[node.val] = node.neighbors
            for neighbor in curr.neighbors:
                if neighbor not in adj_dict:
                    adj_dict[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                adj_dict[curr].neighbors.append(adj_dict[neighbor])

                
        return adj_dict[node]


         



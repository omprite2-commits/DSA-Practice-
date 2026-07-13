from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        # 1. Adjacency list banayein tree ko represent karne ke liye
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. BFS chalakar root (1) se sabse door wala node (max depth) dhoondhein
        queue = deque([(1, 0)])
        visited = {1}
        max_edges = 0
        
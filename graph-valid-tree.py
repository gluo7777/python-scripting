import math
from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1: return True

        # create adjacency matrix
        adj = {}
        for i,j in edges:
            if not i in adj: adj[i] = [j]
            else: adj[i].append(j)
            if not j in adj: adj[j] = [i]
            else: adj[j].append(i)

        # dfs
        # keep track of visited nodes
        visited_nodes = set()

        def dfs(i: int, prev: int = math.nan) -> bool:
            """
            @return true if no cycle, false otherwise
            """
            if i in visited_nodes: return False
            visited_nodes.add(i)
            for j in adj[i]:
                if prev == j: continue
                elif dfs(j,i): continue
                else: return False
            return True

        # perform DFS on any node
        if not dfs(0): return False

        # first DFS should have visited all nodes
        # if any nodes unvisited, then graph is not a valid tree
        for i in adj.keys():
            if i not in visited_nodes: return False

        return True
        
s = Solution()
print(s.valid_tree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(s.valid_tree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

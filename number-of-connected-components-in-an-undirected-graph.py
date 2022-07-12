from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
    # create adjacency matrix
    adj = {}
    for x,y in edges:
        if x not in adj: adj[x] = [y]
        else: adj[x].append(y)
        if y not in adj: adj[y] = [x]
        else: adj[y].append(x)
    # perform DFS/BFS against adjacency matrix
    visited = set()
    def dfs(i: int):
        if i in visited:
            return
        visited.add(i)
        for j in adj[i]:
            dfs(j)
    count = 0
    for i in adj:
        if not i in visited:
            count += 1
            dfs(i)
    return count

print(countComponents(8,[[0,1],[1,2],[3,4],[5,6],[6,7]]))
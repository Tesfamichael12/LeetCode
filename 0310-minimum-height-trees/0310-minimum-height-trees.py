class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        qu = deque( i for i in range(n) if len(graph[i]) == 1) # if node is a leaf node

        rem = n
        while rem > 2:
            rem -= len(qu)
            for _ in range(len(qu)):
                leaf = qu.popleft()
                nbr = graph[leaf].pop()
                graph[nbr].remove(leaf)
                if len(graph[nbr]) == 1:
                    qu.append(nbr)
        
        return list(qu)
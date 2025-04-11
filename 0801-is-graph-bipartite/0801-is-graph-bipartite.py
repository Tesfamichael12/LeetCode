class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = [-1] * len(graph) 
        visited = set()
        def dfs(node):
            visited.add(node)

            for n in graph[node]:
                if color[n] == color[node]: 
                    color[n] = -1 * color[node]

                if n not in visited:
                    dfs(n)

        for node in range(len(graph)):
            if node not in visited:
                dfs(node)

        for node in range(len(graph)):
            for n in graph[node]:
                if color[node] == color[n]:
                    return False
        return True
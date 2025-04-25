class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v in richer:
            graph[u].append(v) # u - richer to v - poorer
        
        visited = [-1] * len(quiet)
        ans = []
        def dfs(node):
            visited[node] = 1
            for child in graph[node]:
                if visited[child] == -1:
                    if dfs(child):
                        return True
                elif visited[child] == 1:
                    return True

            visited[node] = 0
            ans.append(node)
            return False
        
        for i in range(len(quiet)):
            if visited[i] == -1:
                dfs(i)
        ans = ans[:: -1]

        quietest = [ i for i in range(len(quiet))]
        # Relaxation ( like Dijkstra / DP style ) propaget from richer to the poorer
        for person in ans:
            for poorer in graph[person]:
                if quiet[quietest[person]] < quiet[quietest[poorer]]:
                    quietest[poorer] = quietest[person]
        
        return quietest
       
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for _ in range(n)] # graph[node][color]
        for u, v in redEdges:
            graph[u][0].append(v)
        for u, v in blueEdges:
            graph[u][1].append(v)
        
        qu = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)])

        ans = [-1] * n
        dist = 0
        while qu:
            for _ in range(len(qu)):
                cur_node, cur_color = qu.popleft()

                if ans[cur_node] == -1 : ans[cur_node] = dist

                next_color = 1 - cur_color
                for adj in graph[cur_node][next_color]:
                    if (adj, next_color) not in visited:
                        visited.add((adj, next_color))
                        qu.append((adj, next_color))

            dist += 1
        
        return ans
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for _ in range(n)] # graph[node][color]
        for u, v in redEdges:
            graph[u][0].append(v)
        for u, v in blueEdges:
            graph[u][1].append(v)
        
        def bfs(node, end, start_color):
            qu = deque()
            qu.append((node, start_color, 0)) # node, start_color and steps
            visited = set((node, start_color))

            while qu:
                cur_node, next_color, steps = qu.popleft()
                if cur_node == end: return steps

                next_color = 1 - next_color
                for adj in graph[cur_node][next_color]:
                    if (adj, next_color) not in visited:
                        visited.add((adj, next_color))
                        qu.append((adj, next_color, steps + 1))
                    
            return -1

        ans = [0]  * n
        for i in range(n):
            red = bfs(0, i, 0)
            blue = bfs(0, i, 1)

            if red > -1 and blue > -1:
                ans[i] = min(red, blue)
            else:
                ans[i] = max(red, blue)

        return ans 
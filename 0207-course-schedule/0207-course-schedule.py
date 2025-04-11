class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[v].append(u)
    
        visited = set()
        path = [0] * numCourses
        def dfs(node):
            visited.add(node)
            path[node] = 1
            for n in graph[node]:
                if n not in visited:
                    if dfs(n):
                        return True

                elif path[n] == 1:
                    return True

            path[node] = 0
            return False
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True
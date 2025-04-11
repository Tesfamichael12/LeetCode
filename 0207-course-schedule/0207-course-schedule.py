class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq) # directed graph ( c -> p)

        visited = [-1] * numCourses # -1 = unvisited, 0 = visited not in path, 1 visited & in path
        def dfs(node):
            visited[node] = 1

            for adj in graph[node]:
                if visited[adj] == -1: # node is not visited
                    if dfs(adj):
                        return True
                elif visited[adj] == 1: # if adj is visited and is in the current path
                    return True
            
            visited[node] = 0 # remove the node from the path
            return False

        for i in range(numCourses):
            if visited[i] == -1: # node is not visited
                if dfs(i):
                    return False
        return True
        
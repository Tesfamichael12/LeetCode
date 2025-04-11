class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq) # directed graph ( c -> p)

        visited = set()
        path = [0] * numCourses
        def dfs(node):
            visited.add(node)
            path[node] = 1 # add to the current path

            for adj in graph[node]:
                if adj not in visited:
                    if dfs(adj):
                        return True
                elif adj in visited and path[adj] == 1: # if adj is visited and is in the current path
                    return True
            
            path[node] = 0 # remove the node from the path
            return False

        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        return True
        
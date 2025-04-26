class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
                graph[u].append(v)
                indegree[v] += 1
        
        qu = deque( i for i in range(numCourses) if i not in indegree)

        prereq = [ set() for _ in range(numCourses)]
        while qu:
            cur = qu.popleft()
            for child in graph[cur]:
                prereq[child] |= prereq[cur]
                prereq[child].add(cur)

                indegree[child] -= 1
                if indegree[child] == 0:
                    qu.append(child)

        return [ u in prereq[v] for u, v in queries ]
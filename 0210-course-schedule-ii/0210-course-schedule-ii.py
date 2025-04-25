class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        indegree = defaultdict(int)
        for val in graph.values():
            for node in val:
                indegree[node] += 1

        qu = deque()
        for i in range(numCourses):
            if i not in indegree:
                qu.append(i)
        ans = []
        while qu:
            for _ in range(len(qu)):
                cur = qu.popleft()
                ans.append(cur)
                for child in graph[cur]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        qu.append(child)
                        del indegree[child]

        if len(ans) != numCourses:
            return []
        return ans
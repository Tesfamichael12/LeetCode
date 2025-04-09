class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            graph[eq[0]].append([eq[1], values[i]])
            graph[eq[1]].append([eq[0], 1 / values[i]])
        
        def dfs(src, target):
            if src not in graph: return -1
            if src == target: return 1

            stack = [(src, 1)]
            seen = set()
            while stack:
                node, val = stack.pop()
                if node == target: return val
                seen.add(node)

                for n, w in graph[node]:
                    if n not in seen:
                        stack.append((n, val * w))
            return -1

        return [dfs(node, target) for node, target in queries]
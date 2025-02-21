class Solution:
    def restoreArray(self, Pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in Pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        res = []

        for node, ne in graph.items():
            if len(ne) == 1:
                res = [node, ne[0]]
                break
        
        while len(res) < len(Pairs) + 1:
            last, prev = res[-1], res[-2]

            candidates = graph[last]
            next_el = candidates[0]if candidates[0] != prev else candidates[1]
            res.append(next_el)

        return res
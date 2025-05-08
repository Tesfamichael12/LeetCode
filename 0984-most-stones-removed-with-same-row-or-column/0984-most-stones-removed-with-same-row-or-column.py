class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        par = defaultdict(list)
        size = defaultdict(int)
        for i, j in stones:
            rows[i].append((i, j))
            cols[j].append((i, j))
            par[(i, j)] = (i, j)
            size[(i, j)] = 1

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if size[rx] > size[ry]:
                    par[ry] = rx
                    size[rx] += size[ry]
                else:
                    par[rx] = ry
                    size[ry] += size[rx]

                return True
            else:
                return False # if they are already in the same component
        
        edges = 0
        for val in rows.values():
            first = val[0]
            for next in val[1:]:
                if union(first, next):
                    edges += 1
        for val in cols.values():
            first = val[0]
            for next in val[1:]:
                if union(first, next):
                    edges += 1
     
        return edges

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, store):
            if len(store) == k:
                res.append(store[:])

            for j in range(i, n+1):
                store.append(j)
                backtrack(j+1, store)
                store.pop()
        
        backtrack(1, [])
        return res
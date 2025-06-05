class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        px = [0]
        for num in arr:
            px.append(px[-1] ^ num)

        res = []
        for l, r in queries:
            ans = px[r+1] ^ px[l]
            res.append(ans)
        
        return res
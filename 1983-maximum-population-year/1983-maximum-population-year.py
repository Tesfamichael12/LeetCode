class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        px = [0] * 2051
        for l, r in logs:
            px[l] += 1
            px[r] -= 1
        
        px = list(accumulate(px))
        mx = max(px)

        for i in range(len(px)):
            if px[i] == mx:
                return i
        
        return -1
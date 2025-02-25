class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key= lambda x : x[1])
        mx = nums[-1][1]
        px = [0] * (mx + 2)

        for l, r in nums:
            px[l] += 1
            px[r+1] -= 1
        
        px = list(accumulate(px))
        res = 0
        for i in range(len(px)):
            if px[i] > 0:
                res += 1
        
        return res
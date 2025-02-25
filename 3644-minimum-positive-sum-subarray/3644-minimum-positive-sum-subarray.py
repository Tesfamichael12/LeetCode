class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mn = float('inf')
        px = [0] + list(accumulate(nums))
        print(px)
        for i in range(1,len(px)):
            for j in range(i + l-1, min(i + r, len(px))):
                res = px[j] - px[i-1]
                if res > 0:
                    mn = min(mn, res)
        
        return mn if mn != float('inf') else -1
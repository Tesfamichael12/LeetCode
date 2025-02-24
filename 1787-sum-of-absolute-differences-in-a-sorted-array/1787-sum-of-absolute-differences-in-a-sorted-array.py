class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        px = [0] * n
        sx = [0] * n
        px[0] = nums[0]
        sx[-1] = nums[-1]

        for i in range(1, n):
            px[i] = px[i-1] + nums[i]
            
        for i in range(n-2, -1, -1):
            sx[i] = sx[i+1] + nums[i]
        
        # print(sx, px)

        res = []
        for i in range(n):
            ans = (nums[i] * i - px[i]) + (sx[i] - nums[i] * (n - i -1))
            res.append(ans)
        
        return res
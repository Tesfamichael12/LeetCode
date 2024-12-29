class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for x in count:
            if x+1 in count:
                res = max(res, count[x] + count[x+1])
        
        return res
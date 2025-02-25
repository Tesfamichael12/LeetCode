class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        px = list(accumulate(nums))
        nums.reverse()
        sx = list(accumulate(nums))
        sx.reverse()
        for i in range(len(nums)):
            if px[i] == sx[i]:
                return i
        
        return -1
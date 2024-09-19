class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for n in nums:
            if nums[l] != n:
                nums[l+1] = n
                l+=1
        return l + 1

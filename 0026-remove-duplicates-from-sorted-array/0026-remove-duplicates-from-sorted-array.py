class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for n in nums:
            if i < 1 or n > nums[i - 1]: # for any number of duplicates allowed we can generalize it as if i < k or nums[i - k] where k is the number of duplicates allowed 
                nums[i] = n
                i += 1
        return i
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = L =0
        for R in range(n - 2): 
            if nums[R] == 0:  
                nums[R] = 1 - nums[R]
                nums[R + 1] = 1 - nums[R + 1]
                nums[R + 2] = 1 - nums[R + 2]
                count += 1

            if nums[L] == 1: L+= 1
        
        # check if all elements are 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return -1
        return count

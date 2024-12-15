class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_dict = {}
        min_val = min(nums)
        for i in range(min_val, len(nums) + 1):
            my_dict[i] = 0
        
        for num in nums:
            my_dict[num] += 1
        
        for key, val in my_dict.items():
            if val == 0:
                return key
        else:
            return 0
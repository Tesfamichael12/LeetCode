class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candidate = nums[0]
        for n in nums:
            if count == 0:
                candidate = n
            
            count += 1 if candidate == n else -1
        
        return candidate
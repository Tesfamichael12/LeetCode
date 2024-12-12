class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for n in nums:
            if n == candidate:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                candidate = n
                count += 1
        
        return candidate
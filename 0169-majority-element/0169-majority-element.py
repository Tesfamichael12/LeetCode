class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candidate = nums[0]
        for n in nums:
            if n == candidate:
                count += 1
            else:
                if count:
                    count -= 1
                else:
                    candidate = n
                    count += 1
        
        return candidate
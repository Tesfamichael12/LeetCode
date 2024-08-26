class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap[n] + 1 if n in hashmap else 1
        majority = 1
        num = nums[0]
        for n in set(nums):
            if hashmap[n] > majority:
                num = n
                majority = hashmap[n]
        
        return num
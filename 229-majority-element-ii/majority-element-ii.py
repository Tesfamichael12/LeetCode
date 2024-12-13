from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for key, val in count.items():
            if val > len(nums) / 3:
                res.append(key)
        
        return res
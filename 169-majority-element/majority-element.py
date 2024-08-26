class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums) // 2
        for key, value in count.items():
            if value > n:
                return key
        
        return 0
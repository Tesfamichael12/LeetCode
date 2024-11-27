class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for n in nums:
            if not(count[n] == 3):
                return n
        return -1 
            
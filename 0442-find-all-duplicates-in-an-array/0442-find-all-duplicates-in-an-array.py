class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for key, val in count.items():
            if val == 2:
                res.append(key)
        
        return res
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        new = sorted(nums)
        out = []
        
        for num in nums:
            
            out.append(new.index(num))
        
        return out
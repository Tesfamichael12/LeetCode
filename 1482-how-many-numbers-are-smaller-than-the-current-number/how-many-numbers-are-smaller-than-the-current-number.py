class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        new = sorted(nums)
        out = []
        
        print(new)
        for num in nums:
            
            out.append(new.index(num)) # the index method returns the first occurance of num, which assures that it will append only the numbers less than num if duplicates exist
        
        return out
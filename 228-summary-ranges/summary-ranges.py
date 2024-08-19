class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        i = 0
        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            
            if start == nums[i]:
                out.append(str(start))
            else:
                out.append(f"{start}->{nums[i]}")
            i += 1
        
        return out

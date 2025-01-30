class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        l, r = 0, len(nums) -1 
        while l < r:
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r -= 1
            
        if l == r:
            res.append(nums[l])

        return res
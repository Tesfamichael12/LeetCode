class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_w = z_count = l = 0
        
        
        for r in range(n):
            if nums[r] == 0: z_count +=1 

            while z_count > k:
                if nums[l] == 0: z_count -= 1
                l += 1
            
            window = r - l + 1
            max_w = max(max_w, window)
        
        return max_w
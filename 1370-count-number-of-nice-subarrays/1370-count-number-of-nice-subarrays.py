class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = odd = 0
        L = M = 0
        for R in range(len(nums)):
            if nums[R] % 2 != 0:
                odd += 1
            
            while odd > k:
                if nums[L] % 2 != 0:
                    odd -= 1
                L += 1
                M = L
            
            if odd == k:
                while not nums[M] % 2:
                    M += 1
                res += (M - L + 1)
        
        return res
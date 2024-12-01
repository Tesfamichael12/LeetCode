class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = 0
            L, R = 0, 0
            for R in range(len(nums)):
                if nums[R] % 2 != 0:
                    k -= 1
                while k < 0:
                    if nums[L] % 2 != 0:
                        k += 1
                    L += 1
                count += R - L + 1
            return count
            
        return atMost(k) - atMost(k-1)
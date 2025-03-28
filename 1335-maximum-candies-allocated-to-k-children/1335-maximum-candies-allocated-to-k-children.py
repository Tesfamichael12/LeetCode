class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(pile):
            cnt = 0
            for n in candies:
                cnt += n // pile if n >= pile else 0
            
            return cnt >= k
        
        l, r = 1, max(candies)
        while l <= r:
            mid = (l+r)//2

            if possible(mid):
                l = mid + 1
            else:
                r = mid - 1
            
        return r
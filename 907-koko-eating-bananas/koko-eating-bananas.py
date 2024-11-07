class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L, R = 1, max(piles)     # max steps 30 => 10^9 / 2^30 = 1
        while L <= R:
            mid = L + (R - L) // 2  
            
            time = sum(math.ceil(pile / mid) for pile in piles)
            if time <= h:
                R = mid - 1
            else:
                L = mid + 1
        return L
            
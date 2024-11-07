class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L, R = 1, max(piles)
        while L <= R:
            mid = L + (R - L) // 2  # avoid any overflow
            
            time = sum(math.ceil(pile / mid) for pile in piles)
            if time <= h:
                R = mid - 1
            else:
                L = mid + 1
        return L
            
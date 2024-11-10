class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        k = 1
        while L <= R:
            mid = (L+R)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid )
            if time <= h:
                k = mid 
                R = mid - 1
            else:
                L = mid + 1
        return k
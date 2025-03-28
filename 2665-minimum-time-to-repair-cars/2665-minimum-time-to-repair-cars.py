class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def possible(time):
            cnt = 0
            for n in ranks:
                cnt += int(sqrt(time / n))
            
            return cnt >= cars

        l, r = 1, max(ranks) * cars**2
        while l <= r:
            mid = (l + r) // 2

            if possible(mid):
                r = mid - 1
            else: 
                l = mid + 1
            
        return l
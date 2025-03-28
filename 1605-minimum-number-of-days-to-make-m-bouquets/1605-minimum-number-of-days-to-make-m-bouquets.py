class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def checker(mid):
            bu , cnt = 0, 0
            for n in bloomDay:
                if n <= mid:
                    bu += 1
                else: 
                    bu = 0
                
                if bu == k: 
                    cnt += 1
                    bu = 0
            
            return cnt >= m

        l, r = 1, max(bloomDay)
        while l <= r:
            mid = (l+r)//2

            if checker(mid):
                r = mid - 1
            else:
                l = mid + 1
                
        return l if checker(l) else -1
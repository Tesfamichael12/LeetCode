class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        max_days = max(bloomDay)
        min_days = -1
        L, R = 0, max_days
        while L <= R:
            mid = (L+R)//2
            count = 0
            m_count = 0
            for bloom in bloomDay:
                if mid >= bloom:
                    count += 1
                    if count >= k:
                        m_count += 1
                        count = 0
                else:
                    count = 0
            if m_count >= m:
                min_days = mid
                R = mid - 1  
            else:
                L = mid + 1
            
        return min_days
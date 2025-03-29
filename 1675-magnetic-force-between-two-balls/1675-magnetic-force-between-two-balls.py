class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        def possible(dis):
            cnt = 1
            last = pos[0]
            for i in range(1, len(pos)):
                if pos[i] >= last + dis:
                    cnt += 1
                    last = pos[i]
            
            return cnt >= m
        
        pos.sort()
        l, r = 0, pos[-1] - pos[0]
        while l <= r:
            mid = (l + r) // 2

            if possible(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
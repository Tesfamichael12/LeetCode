class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        qu = deque()
        
        l = 0
        for r in range(len(nums)):
            while qu and qu[-1][0] < nums[r]:
                qu.pop()
            
            qu.append((nums[r], r))
            if r - l + 1 == k:
                res.append(qu[0][0])
                if l == qu[0][1]:
                    qu.popleft()
                l += 1

        return res

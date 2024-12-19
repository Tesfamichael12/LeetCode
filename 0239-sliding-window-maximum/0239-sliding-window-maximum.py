from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # store useful el in decearsing order [10, 5, 3, 1]
        res = []
        l = 0
        for r, num in enumerate(nums):
            # remove el which are out of the window
            while dq and dq[0] < l:
                dq.popleft()

            # remove all the elements that are smaller
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(r)

            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1
        return res
            

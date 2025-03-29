class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def possible(k):
            ran = [0] * (len(nums) + 2)
            for i in range(k):
                l, r, val = queries[i]
                ran[l] += val
                ran[r+1] -= val
            
            ran = list(accumulate(ran))
            arr = nums[:]
            for i in range(len(nums)):
                arr[i] = max(0, arr[i] - ran[i])
            
            return len(set(arr)) == 1 and arr[0] == 0

        l, r = 0, len(queries)
        ans = -1
        while l <= r:
            mid = (l + r) // 2

            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
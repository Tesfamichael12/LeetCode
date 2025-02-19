class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort(key = lambda x : x[1])
        mx = requests[-1][1]
        
        prifix = [0] * (mx + 2)

        for re in requests:
            l, r = re
            prifix[l] += 1
            prifix[r+1] -= 1

        prifix = list(accumulate(prifix))

        prifix.sort(reverse = True)
        mx = max(prifix)
        indx = prifix.index(mx)
        prifix = prifix[indx:]

        nums.sort(reverse=True)
        res = 0
        for i in range(len(prifix)):
            if i >= len(nums): break
            res += (nums[i] * prifix[i])
        
        return res % (10**9 + 7)
class Solution(object):
    def __init__(self):
        self.dp = []

    def sol(self, nums, i, p):
        n = len(nums)
        if i >= n:
            if 0 <= p < n:
                return nums[p]
            return 0
        if i == n - 1:
            maxi = nums[i]
            if 0 <= p < n:
                maxi = max(maxi, nums[p])
            return maxi
        if self.dp[i][p] != -1:
            return self.dp[i][p]
        ans = int(1e11)
        j = i + 1
        ans = min(ans, max(nums[p], nums[i]) + self.sol(nums, i + 2, i + 1))
        ans = min(ans, max(nums[p], nums[i + 1]) + self.sol(nums, i + 2, i))
        ans = min(ans, max(nums[i], nums[i + 1]) + self.sol(nums, i + 2, p))
        self.dp[i][p] = ans
        return ans

    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            if n == 1:
                return nums[-1]
            return max(nums[0], nums[1])
        self.dp = [[-1] * (n + 1) for _ in range(n + 1)]
        ans = int(1e11)
        ans = self.sol(nums, 1, 0)
        return ans
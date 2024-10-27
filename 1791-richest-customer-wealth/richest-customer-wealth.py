class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for n in accounts:
            w = sum(n)
            max_wealth = max(max_wealth, w)
        return max_wealth
                
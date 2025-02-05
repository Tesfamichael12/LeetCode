class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_val = sum(accounts[0])
        for account in accounts:
            max_val = max(max_val, sum(account))
        
        return max_val
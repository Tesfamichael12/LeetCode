class Solution:
    def balancedStringSplit(self, s: str) -> int:
        mx = 0
        cnt = 0
        for ch in s:
            if ch == 'R':
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                mx += 1
        
        return mx
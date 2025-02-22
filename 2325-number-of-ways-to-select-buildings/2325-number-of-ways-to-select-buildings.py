class Solution:
    def numberOfWays(self, s: str) -> int:
        count_0 = 0
        count_1 = 0
        count_01 = 0  
        count_10 = 0  
        total = 0

        for char in s:
            if char == "0":
                count_0 += 1 
                count_10 += count_1  
                total += count_01 
            elif char == "1":
                count_1 += 1 
                count_01 += count_0  
                total += count_10  
        
        return total

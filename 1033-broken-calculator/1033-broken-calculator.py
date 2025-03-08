class Solution:
    def brokenCalc(self, val: int, t: int) -> int:
        steps = 0
        while t > val:
            if t % 2 == 0:
                t //= 2  
            else:
                t += 1  
            steps += 1
        
        return steps + (val - t)  
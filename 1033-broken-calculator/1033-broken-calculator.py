class Solution:
    def brokenCalc(self, val: int, t: int) -> int:
        steps = 0
        while t > val:
            if t % 2 == 0:
                t //= 2  # Reverse doubling by halving t
            else:
                t += 1  # Make it even to prepare for division by 2
            steps += 1
        
        # Now, we can only subtract to match val
        return steps + (val - t)  # Decrement val to match t

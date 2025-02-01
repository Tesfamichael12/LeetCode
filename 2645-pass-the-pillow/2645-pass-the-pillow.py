class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr_time = 0
        direction = 1
        i = 1
        while curr_time < time:
            if 0 < i + direction <= n:
                i += direction
                curr_time += 1
            else:
                direction *= -1
        
        return i
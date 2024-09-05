class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxval = count = 0
        for i, flip in enumerate(flips):
            maxval = max(maxval, flip)
            if maxval == i + 1: # since flip(maxval) is a 1-indexed and i is 0-indexed 
                count += 1
                
        return count
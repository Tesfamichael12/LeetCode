class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors) # keep the orginal length for latter
        count = 0

        # extend the colors array to simulate a circular pattern 
        colors.extend(colors[:2])

        for r in range(n): 
            if colors[r] == colors[r+2] and colors[r] != colors[r+1]:
                count += 1
                
        return count

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        # check the end colors 
        if len(colors) > 2:
            if colors[0] != colors[1] and colors[1] == colors[-1]:
                count += 1
            if colors[-2] != colors[-1] and colors[-2] == colors[0]:
                count += 1
        
        l, r = 0, 0
        k = 3
        for r in range(len(colors)):
            if r - l + 1 == 3:
                l += 1
            if r < len(colors) - 1 and colors[l] == colors[r+1] and colors[l] != colors[r]:
                count += 1

        return count
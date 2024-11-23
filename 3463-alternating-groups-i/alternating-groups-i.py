class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        # extend the colors array to simulate a circular pattern 
        circular_colors = colors + colors[:2] # colors.extends(colors[:2])
        
        for r in range(len(colors)): 
            if circular_colors[r] == circular_colors[r+2] and circular_colors[r] != circular_colors[r+1]:
                count += 1
                
        return count

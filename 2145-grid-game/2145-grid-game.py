class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])  
        
        # Calculate the prefix sum for both rows
        prefix_top = [0] + list(accumulate(grid[0]))
        prefix_bottom = [0] + list(accumulate(grid[1]))

        res = float('inf')
        for i in range(1, n+1):
            # Robot 1 breaks at column `i`
            # Top path remaining for Robot 2
            top_remaining = prefix_top[-1] - prefix_top[i]
            # Bottom path remaining for Robot 2
            bottom_remaining = prefix_bottom[i - 1] 
            
            # Robot 2's maximum possible score if Robot 1 splits at `i`
            robot2_score = max(top_remaining, bottom_remaining)
            res = min(res, robot2_score)
        
        return res

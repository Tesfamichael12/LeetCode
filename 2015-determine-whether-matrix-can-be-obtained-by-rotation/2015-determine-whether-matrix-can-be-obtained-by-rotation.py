class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(nums):
            new = [[0]*len(nums) for _ in range(len(nums[0])) ]
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    new[j][i] = nums[i][j] 
            
            for i, row in enumerate(new):
                row.reverse()
                new[i] = row
            
            return new
        
        if mat == target: return True
        for _ in range(3):
            mat = rotate(mat)
            if mat == target: return True
        
        return False

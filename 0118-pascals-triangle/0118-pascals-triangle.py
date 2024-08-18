class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        # intialize the pascal array all with 1 value
        pascal = [ [1] * (i + 1) for i in range(numRows)]
        
        # Build the pascal triangle
        for i in range(2, numRows): # start from second row
            for j in range(1, i):   # start form second column upto second of last number
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        
        return pascal
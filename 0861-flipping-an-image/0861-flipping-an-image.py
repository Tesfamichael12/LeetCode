class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev = []
        for row in image:
            row.reverse()
            rev.append(row)
        
        for i in range(len(rev)):
            for j in range(len(rev[0])):
                if rev[i][j] == 1:
                    rev[i][j] = 0
                else:
                    rev[i][j] = 1
        
        return rev
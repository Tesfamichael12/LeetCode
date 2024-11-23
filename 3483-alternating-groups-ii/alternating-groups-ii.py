class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0

        colors.extend(colors[:k-1]) # if k = 3 we add 2 numbers like the above question
        print(colors)

        L = 0
        for R in range(1, len(colors)):
            
            if colors[R] == colors[R-1]:
                L = R
            if R - L + 1 == k:
                count += 1
                L += 1

        return count
            
            
            
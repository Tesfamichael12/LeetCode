class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key= lambda p: p[0])
        maxwidth = 0
        for i in range(1, len(points)):
            maxwidth = max(maxwidth, points[i][0] - points[i-1][0])
        
        return maxwidth
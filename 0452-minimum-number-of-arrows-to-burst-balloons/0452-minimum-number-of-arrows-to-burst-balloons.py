class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        
        count = 1
        i = 0
        while i < n - 1:
            if points[i+1][0] > points[i][1] :
                count += 1
            else:
                points[i+1][1] = min(points[i+1][1], points[i][1])

            i += 1

        return count 
                

            
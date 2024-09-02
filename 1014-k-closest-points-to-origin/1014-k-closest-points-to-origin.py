class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, (x, y) in enumerate(points):
            d = x**2 + y**2  
            distances.append((d, i))  
        
        # Sort distances list by the first element of the tuple (the distance)
        distances.sort()

        res = []
        for i in range(k):
            res.append(points[distances[i][1]])
        
        return res

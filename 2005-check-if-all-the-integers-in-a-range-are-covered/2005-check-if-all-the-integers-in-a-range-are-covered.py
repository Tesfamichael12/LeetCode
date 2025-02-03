class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        range_ = set()
        cover = set()

        for i in range(left, right+1):
            cover.add(i)
        
        for range_i in ranges:
            for i in range(range_i[0], range_i[1]+1):
                range_.add(i)
        
        return cover <= range_
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            res.extend([i+1, n])
            
            arr = arr[:i:-1] + arr[:i]
        
        return res
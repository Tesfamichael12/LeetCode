class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        max_val = arr[-1]
        res[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            res[i] = max_val
            max_val = max(max_val, arr[i])
        
        return res
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = clen = 0
        for i in range(len(arr)):
            if i >= 2 and (arr[i-2] < arr[i-1] > arr[i] or arr[i-2] > arr[i-1] < arr[i]):
                clen += 1
            elif i >= 1 and arr[i-1] != arr[i]:
                clen = 2
            else:
                clen = 1
            
            max_len = max(max_len, clen)
    
        return max_len
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        px = [0]
        for num in arr:
            px.append(px[-1] ^ num)
        
        res = 0
        for i in range(1, len(px)):
            l = px[i - 1]
            for j in range(i + 1 , len(px)):
                r = px[j]

                if l ^ r == 0:
                    res += j - i 
        
        return res
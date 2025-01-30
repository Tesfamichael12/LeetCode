class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        largest = strs[0]
        smallest = strs[0]

        for c in strs:
            if largest < c:
                largest = c
            if smallest > c:
                smallest = c
        
        i = 0
        while i < len(smallest):
            if largest[i] == smallest[i]:
                i += 1
            else: break
        
        return smallest[:i]

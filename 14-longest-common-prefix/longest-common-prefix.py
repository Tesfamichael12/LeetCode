class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        largest = smallest = strs[0]
        for s in strs:
            if s > largest:
                largest = s
            if s < smallest:
                smallest = s
        
        for c in range(min(len(largest), len(smallest))):
            if largest[c] == smallest[c]:
                common += largest[c]
            else: break
        
        return common
        
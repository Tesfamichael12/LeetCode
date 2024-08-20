class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i 

        return len(citations) # if we have a citaions list like 3,3,3 
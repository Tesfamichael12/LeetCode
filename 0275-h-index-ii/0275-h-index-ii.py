class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L, R = 0, len(citations) - 1
        while L <= R:
            mid = (L + R) // 2
            # Check if the number of citations from mid to the end is at least the citations[mid]
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            elif citations[mid] < len(citations) - mid:
                L = mid + 1
            else:
                R = mid - 1
        # If no exact match is found, return the number of papers with at least l citations
        return len(citations) - L

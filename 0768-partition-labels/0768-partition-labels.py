class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = [0] * 26
        for idx, val in enumerate(s):
            end_idx[ord(val) - ord('a')] = idx

        res = []
        start = end = 0
        for i, val in enumerate(s):
            end = max(end, end_idx[ord(val) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        
        return res

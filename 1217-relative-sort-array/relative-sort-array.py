class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count = Counter(arr1)
        out = []
        for n in arr2:
            new = [n] * count[n]
            out.extend(new)
            del count[n]

        sort_count = dict(sorted(count.items()))
        for num, i in sort_count.items():
            new = [num] * i
            out.extend(new)
        return out
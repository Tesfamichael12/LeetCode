class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        arr_2_set = set(arr2)
        counting = []
        for n in arr2:
            counting.extend([n] * count[n])

        temp = []
        for n in arr1:
            if n not in arr_2_set:
                temp.append(n)
        
        temp.sort()
        counting.extend(temp)
        
        return counting

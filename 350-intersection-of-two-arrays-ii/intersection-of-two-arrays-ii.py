class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        for num in count1:
            if num in count2:
                freq = min(count1[num], count2[num])

                out.extend([num] * freq)

        return out

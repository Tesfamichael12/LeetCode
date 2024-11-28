class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Count sums of pairs in nums1 and nums2
        sum_count = Counter(a + b for a in nums1 for b in nums2)
        print(sum_count)

        # Find complementary sums in nums3 and nums4
        count = 0
        for c in nums3:
            for d in nums4:
                complement = -(c + d)
                count += sum_count.get(complement, 0)
        
        return count

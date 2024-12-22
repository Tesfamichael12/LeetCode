class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)

        for i, num in enumerate(nums):
            if num in seen:
                if abs(seen[num] - i) <= k:
                    print(seen[num], i)
                    return True
            
            seen[num] = i
        
        return False
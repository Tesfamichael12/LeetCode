class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        res = []

        # Sort the keys of the counter
        for num in sorted(count):
            # Check if there are enough doubles for the current number
            if count[num] > count[num * 2]:
                return []
            # Special case for 0: pair the 0s in the array
            if num == 0:
                if count[num] % 2 != 0:
                    return []
                res.extend([0] * (count[num] // 2))
            else:
                # Add the current number to the result list
                res.extend([num] * count[num])
                count[num * 2] -= count[num]

        return res

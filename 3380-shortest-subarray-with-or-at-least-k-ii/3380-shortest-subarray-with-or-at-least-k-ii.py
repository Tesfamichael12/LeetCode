class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # OR operator | is always set bit operation, so we sall use counter to count how many times that bit have been set 

        l = 0
        mask = 0
        counter = { i : 0 for i in range(36)} # upper bound for 10 ^ 9 => (2^4)^9 = 2 ^ 36
        min_len = float('inf')
        for r in range(len(nums)):
            
            binary = bin(nums[r])[2:][::-1]
            for i, c in enumerate(binary): # max len is 36
                if c == '1': 
                    counter[i] += 1
                    mask |= (1 << i) # set bit

            while l <= r and mask >= k:
                min_len = min(min_len, r - l + 1)

                binary_rep = bin(nums[l])[2:][::-1]
                for i, c in enumerate(binary_rep): # max len is 36
                    if c == '1': 
                        counter[i] -= 1
                        if counter[i] == 0:
                            mask &= ~(1 << i) # unset bit
                l += 1
        
        return min_len if min_len != float('inf') else -1
        
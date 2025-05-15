class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        max_bit_lenght = 32

        binary_rep = [0] * (max_bit_lenght)
        for i in range(max_bit_lenght): # max lenght is 32

            set_bit_count = 0
            for num in nums:
                if num < 0:
                    num = (~num + 1)
                if num & (1 << i):
                    set_bit_count += 1

            binary_rep[i] = set_bit_count % 3

        binary_rep.reverse()
        ans = int("".join(map(str, binary_rep)), 2) 
        
        cnt = 0
        for num in nums:
            if num == ans:
                cnt += 1
        
        if cnt > 1 or cnt == 0:
            return -ans
        else:
            return ans
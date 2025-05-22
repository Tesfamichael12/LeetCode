class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1
        a = a & mask
        b = b & mask

        if a < 0:
            a = a & mask
            bin_a = bin(a)[2:][::-1]
        else:
            bin_a = bin(a)[2:][::-1]

        if b < 0:
            b = b & mask
            bin_b = bin(b)[2:][::-1]
        else:
            bin_b = bin(b)[2:][::-1]

        carry = 0
        i, j = 0, 0
        res = []
        while i < len(bin_a) and j < len(bin_b):
            if bin_a[i] == '1' and bin_b[j] == '1':
                if carry == 1:
                    res.append(1)
                else:
                    res.append(0)
                carry = 1

            elif bin_a[i] == '0' and bin_b[j] == '0':
                if carry == 1:
                    res.append(1)
                    carry = 0
                else:
                    res.append(0)
            else:
                if carry == 1:
                    res.append(0)
                else:
                    res.append(1)
            
            i += 1
            j += 1
        
        while i < len(bin_a):
            if bin_a[i] == '1':
                if carry == 1:
                    res.append(0)
                else:
                    res.append(1)
                    carry = 0
            else:
                if carry == 1:
                    res.append(1)
                    carry = 0
                else:
                    res.append(0)
            
            i += 1

        while j < len(bin_b):
            if bin_b[j] == '1':
                if carry == 1:
                    res.append(0)
                else:
                    res.append(1)
                    carry = 0
            else:
                if carry == 1:
                    res.append(1)
                    carry = 0
                else:
                    res.append(0)
                    
            j += 1
        
        if carry == 1:
            res.append(1)

        res.reverse()
        ans = int("".join(map(str, res)), 2)

        max_int = (1 << 31) - 1 # 127 for 8-bits signed integer

        ans &= mask
        if ans > max_int:
            ans -= (1 << 32)
        
        return ans


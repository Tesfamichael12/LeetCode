class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []
        print(ord('a'), ord('i'))
        for ch in s:
            nums.append(ord(ch) - ord('a') + 1)
        print(nums)
        s = "".join(map(str, nums))
        print(s)
        while k > 0:
            sum = 0
            for ch in s:
                sum += int(ch)
            s = str(sum)
            k -= 1
            print(s)
        
        return int(s)

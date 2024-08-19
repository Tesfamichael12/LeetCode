class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = Counter(stones)
        ans = 0
        for ch in jewels:
            if ch in stones:
                ans += stones_dict[ch]
        return ans

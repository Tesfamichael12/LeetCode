class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_type = defaultdict(int)
        maxlen = 0
        l = 0

        for r in range(len(fruits)):
            fruit_type[fruits[r]] += 1

            # keeping a valid window
            while len(fruit_type) > 2:
                fruit_type[fruits[l]] -= 1
                
                if fruit_type[fruits[l]] == 0:
                    del fruit_type[fruits[l]]
                l += 1

            maxlen = max(maxlen, r - l + 1)

        return maxlen
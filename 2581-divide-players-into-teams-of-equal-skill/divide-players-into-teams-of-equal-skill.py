class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        expected_skill = 2 * sum(skill) // n
        skillMap = Counter(skill)

        chemistry = 0
        for s in skill:
            compliment = expected_skill - s
            if compliment not in skillMap or skillMap[compliment] == 0:
                return -1
            chemistry += s * compliment
            skillMap[compliment] -= 1 # we have used it, but we still need s
        
        return chemistry // 2
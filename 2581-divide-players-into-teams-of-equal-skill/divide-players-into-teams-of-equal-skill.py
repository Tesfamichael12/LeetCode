class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        expected_skill = 2 * sum(skill) // len(skill)
        skillMap = Counter(skill)
        chemistry = 0
        for s in skill:
            if skillMap[s] == 0 : continue

            complement = abs(expected_skill - s)
            if skillMap[complement] <= 0:
                return -1
            chemistry += s * abs(expected_skill - s)
            skillMap[s] -= 1
            skillMap[complement] -= 1
        
        return chemistry
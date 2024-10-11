class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        sum = skill[0] + skill[-1]
        for i in range(len(skill) // 2):
            if skill[i] + skill[-1-i] != sum:
                return -1
            res += skill[i] * skill[-1-i]
        return res 
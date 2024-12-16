class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        chemistry = 0
        sum = skill[0] + skill[n-1]
        for i in range(n // 2): # we should go until the middle of the array
            if skill[i] + skill[-1-i] != sum:
                return -1
            chemistry += skill[i] * skill[-1-i]
        return chemistry 


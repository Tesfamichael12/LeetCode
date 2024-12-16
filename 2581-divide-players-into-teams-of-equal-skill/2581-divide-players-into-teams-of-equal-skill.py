class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        r = n - 1
        s = skill[0] + skill[r]
        for l in range(n):
            if skill[l] + skill[r] != s:
                return -1
            r -= 1

        chemistry = 0
        r = n - 1
        for l in range(n):
            chem = skill[l] * skill[r]
            r -= 1
            chemistry += chem
        
        return chemistry // 2

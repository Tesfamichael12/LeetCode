class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        steps = abs(0 - target[0]) + abs(0 - target[1])
        for n in ghosts:
            Gstep = abs(n[0] - target[0]) + abs(n[1] - target[1])
            if Gstep <= steps:
                return False
        return True
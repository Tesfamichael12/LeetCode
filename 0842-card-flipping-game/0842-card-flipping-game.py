class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        common = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                common.add(backs[i])

        # print(common)

        mn = float('inf')
        for b in backs+fronts:
            if b not in common:
                mn = min(mn, b)

        return mn if mn != float('inf') else 0
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        for matche in matches:
            losser = matche[1]
            hashmap[losser] += 1

        lossers = []
        for losser, count in hashmap.items():
            if count == 1:
                lossers.append(losser)

        winners = []
        for matche in matches:
            if matche[0] not in hashmap:
                winners.append(matche[0])
        
        return [sorted(set(winners)), sorted(set(lossers))]
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losser_count = defaultdict(int)
        players = set()

        for winner, losser in matches:
            losser_count[losser] += 1
            players.add(winner)
            players.add(losser)
        
        winners = [winner for winner in players if winner not in losser_count]
        lossers = [player for player, count in losser_count.items() if count == 1]

        return [sorted(winners), sorted(lossers)]
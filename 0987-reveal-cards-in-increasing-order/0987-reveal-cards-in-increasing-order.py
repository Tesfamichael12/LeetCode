class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        res = [0] * n

        q = deque(range(n))
        for n in deck:
            res[q.popleft()] = n
            if q:
                q.append(q.popleft())
        
        return res
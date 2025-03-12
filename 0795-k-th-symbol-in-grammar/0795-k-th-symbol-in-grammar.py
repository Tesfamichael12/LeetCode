class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
            def bit(k):
                if k == 1: return False

                if k % 2:
                    return bit(ceil(k / 2))
                else:
                    return not bit(ceil(k / 2))
            
            return 1 if bit(k) else 0


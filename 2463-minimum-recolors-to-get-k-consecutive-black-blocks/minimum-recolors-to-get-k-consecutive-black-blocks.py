class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L, pro = 0, 0
        minPro = len(blocks)
        for R in range(len(blocks)):
            if blocks[R] == 'W':
                pro += 1 
            if R - L == k-1:
                print(pro, R)
                minPro = min(minPro, pro)
                if blocks[L] == 'W':
                    pro -= 1
                L += 1

        return minPro
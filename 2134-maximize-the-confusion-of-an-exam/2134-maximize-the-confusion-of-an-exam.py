class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def calculateLength(ans: str):
            flips = k 
            max_length = 0

            n = len(answerKey)
            l, r = 0, 0

            while r < n:
                if answerKey[r] == ans:
                    flips -= 1
                while flips < 0:
                    if answerKey[l] == ans:
                        flips += 1
                    l += 1

                max_length = max(max_length, r - l + 1)
                r += 1

            return max_length

        return max(calculateLength('T'), calculateLength('F'))

            

        # max_length = 0
        # flips = k
        # n = len(answerKey)
        # l, r = 0, 0
        # # F -> T
        # while r < n:
        #     if answerKey[r] == 'F':
        #         flips -= 1
        #     while flips < 0:
        #         if answerKey[l] == 'F':
        #             flips += 1
        #         l += 1

        #     max_length = max(max_length, r - l + 1)
        #     r += 1

        # l, r = 0, 0
        # # T -> F
        # while r < n:
        #     if answerKey[r] == 'T':
        #         flips -= 1
        #     while flips < 0:
        #         if answerKey[l] == 'T':
        #             flips += 1
        #         l += 1

        #     max_length = max(max_length, r - l + 1)
        #     r += 1

        # return max_length

        
            
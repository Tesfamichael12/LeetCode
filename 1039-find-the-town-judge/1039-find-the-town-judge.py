class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score=[0]*(n+1)

        for u,v in trust:
            trust_score[u]-=1
            trust_score[v]+=1

        for i in range(1,n+1):
            if trust_score[i]==n-1:
                return i

        return -1
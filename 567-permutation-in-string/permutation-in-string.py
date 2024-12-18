class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_count = Counter(s1)
        s2_count = Counter()
        left = 0
        for i in range(len(s2)):
            s2_count[s2[i]] += 1
            if i >= len(s1)-1:
                if s1_count == s2_count:
                    return True
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left +=1 
        return False
                

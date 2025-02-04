class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)

        for domain in cpdomains:
            n, s = domain.split()
            count[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i + 1:]] += int(n)
        
        res = []
        for s in count:
            val = [str(count[s]), s]
            res.append(" ".join(val))
        
        return res
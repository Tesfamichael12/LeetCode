class Solution:
    def frequencySort(self, s: str) -> str:
        res = list(s)
        count = Counter(res)

        res = dict(sorted(count.items(), key= lambda x: x[1], reverse=True))
        temp = [[key] * i for key, i in res.items()]
        ans = []
        for n in temp:
            ans.extend(n)

        return "".join(ans)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        count = dict(sorted(c.items(), key=lambda item: item[1], reverse=True)) # sort by values
        res = []
        for key in count:
            print(len(res), k)
            if len(res) < k:
                res.append(key)
            else: break

        return res
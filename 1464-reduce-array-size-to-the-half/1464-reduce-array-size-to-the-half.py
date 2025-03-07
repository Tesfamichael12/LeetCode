class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        half = len(arr) // 2
        cnt, sum = 1, 0
        count = dict(sorted(count.items(), key = lambda x : x[1], reverse=True))

        for key, val in count.items():
            sum += val
            if sum >= half:
                return cnt
            
            cnt += 1
        
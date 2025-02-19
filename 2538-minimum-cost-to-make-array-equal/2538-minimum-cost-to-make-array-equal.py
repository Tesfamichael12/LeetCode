class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        prifix = [0] * (len(nums))
        suffix = [0] * (len(nums))

        paris = []
        for n, c in zip(nums, cost):
            paris.append([n, c])
        
        paris.sort(key=lambda x : x[0])

        print(paris)

        cur = cost = 0
        for i in range(1, len(paris)):
            cost += paris[i-1][1]
            cur = (prifix[i-1] + cost * (paris[i][0] - paris[i-1][0]))
        
            prifix[i] = cur

        print(prifix)

        cur = cost = 0
        for i in range(len(paris)-2, -1, -1):
            cost += paris[i+1][1]
            cur = (suffix[i+1] + cost * (paris[i+1][0] - paris[i][0]))
        
            suffix[i] = cur

        print(suffix)

        total = []
        for i in range(len(prifix)):
            total.append(prifix[i] + suffix[i])
        
        return min(total)

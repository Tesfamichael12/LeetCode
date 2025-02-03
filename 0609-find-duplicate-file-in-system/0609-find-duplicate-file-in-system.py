class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dp = defaultdict(list)

        for path in paths:
            val = path.split()
            dir = val[0]
            files = val[1:]
            
            for file in files:
                open_p = file.index('(')
                content = file[open_p + 1:-1]
                value = dir + "/" + file[:open_p]

                dp[content].append(value)
        
        res = []
        for key, val in dp.items():
            if len(val) > 1:
                res.append(val)
        
        return res
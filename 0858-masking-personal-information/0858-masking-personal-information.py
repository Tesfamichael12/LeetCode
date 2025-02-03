class Solution:
    def maskPII(self, s: str) -> str:
        # if s is an email 
        if '@' in s and '.' in s:
            s = s.lower()
            at = s.index('@')
            name = s[:at]
            name = list(name)
            name[1:-1] = "*****"
            name = "".join(name)
            s_new = name + s[at:]
            return s_new
        else:
            r = {'+', '-', '(', ')', ' '}
            res = []
            for c in s:
                if c not in r:
                    res.append(c)
            
            last = res[-4:]
            if len(res) == 10:
                res[:7] = "******"
                
                ans = res[:3] + ["-"] + res[3:6] + ["-"] + last
                # print(ans , res[6:])
                return "".join(ans)

            elif len(res) == 11:
                res[:7] = "******"
                
                ans = ["+*-"] + res[:3] + ["-"] + res[3:6] + ["-"] + last
                return "".join(ans)

            elif len(res) == 12:
                res[:7] = "******"
                
                ans = ["+**-"] + res[:3] + ["-"] + res[3:6] + ["-"] + last
                return "".join(ans)
        
            elif len(res) == 13:
                res[:7] = "******"
                
                ans = ["+***-"] + res[:3] + ["-"] + res[3:6] + ["-"] + last
                return "".join(ans)
        

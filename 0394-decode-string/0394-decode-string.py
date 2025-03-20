class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            res = []
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                
                elif s[i] == '[': # decoding starts
                    i, decode = helper(i + 1)
                    res.extend(decode * num)
                    num = 0
                
                elif s[i] == ']': # end of the current encode block
                    return i, res
                
                else: # regulare chars
                    res.extend(s[i])
                
                i += 1

            return res

        # print(helper(0))
        return "".join(helper(0))
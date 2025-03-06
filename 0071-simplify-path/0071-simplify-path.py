class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        path = list(path.strip().split("/"))
        simple = []
        i = 1
        for s in path:
            if s == "":
                pass
            elif s[0] == '.' :
                print(s)
                if s == '..' and simple:
                    simple.pop()
                elif s != '..' and s != '.':
                    simple.append(s)
            else:
                simple.append(s)

        print(simple)
        return "/" + "/".join(simple)
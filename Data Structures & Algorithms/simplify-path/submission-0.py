class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split("/")
        res = []

        for s in sp:
            if s == "..":
                if res:
                    res.pop()
                else:
                    continue
            elif s =="."or not s:
                continue
            else:
                res.append(s)
        

        print(res)
        return "/"+"/".join(res)
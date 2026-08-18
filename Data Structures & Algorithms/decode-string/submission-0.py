class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(k):
            curr = ""
            i = k

            while i < len(s):
                if s[i].isdigit():
                    currnum = ""

                    while i < len(s) and s[i].isdigit():
                        currnum += s[i]
                        i += 1

                    currnum = int(currnum)

                    # s[i] should be '[' now, so start inside it at i + 1
                    decoded, new_i = helper(i + 1)

                    curr += currnum * decoded
                    i = new_i

                elif s[i] == "]":
                    return curr, i + 1

                else:
                    curr += s[i]
                    i += 1

            return curr, i

        return helper(0)[0]
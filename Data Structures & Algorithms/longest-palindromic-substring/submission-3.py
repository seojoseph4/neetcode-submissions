class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            radius = [0] * n
            c, r = 0, 0
            for i in range(n):
                if i < r:
                    mirror = 2 * c - i
                    radius[i] = min(r - i, radius[mirror])
                while (i + radius[i] + 1 < n and i - radius[i] - 1 >= 0
                       and t[i + radius[i] + 1] == t[i - radius[i] - 1]):
                    radius[i] += 1
                if i + radius[i] > r:
                    r = i + radius[i]
                    c = i
            return radius

        radius = manacher(s)
        maxLen, centerIdx = max((p, i) for i, p in enumerate(radius))
        start = (centerIdx - maxLen) // 2
        return s[start : start + maxLen]
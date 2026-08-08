class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c, l, ans = {}, 0, 0
        for r, x in enumerate(s):
            c[x] = c.get(x, 0) + 1
            while r-l+1-max(c.values()) > k:
                c[s[l]] -= 1; l += 1
            ans = max(ans, r-l+1)
        return ans
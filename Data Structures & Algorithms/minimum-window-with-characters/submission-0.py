class Solution:
    def minWindow(self, s, t):
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        have = {}
        l = count = 0
        ans = ""
        for r, c in enumerate(s):
            have[c] = have.get(c, 0) + 1
            if c in need and have[c] == need[c]:
                count += 1
            while count == len(need):
                if not ans or r - l + 1 < len(ans):
                    ans = s[l:r+1]
                c = s[l]
                have[c] -= 1
                if c in need and have[c] < need[c]:
                    count -= 1
                l += 1
        return ans
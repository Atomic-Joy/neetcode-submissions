class Solution:
    def checkInclusion(self, s1, s2):
        n, need, win = len(s1), [0]*26, [0]*26
        for c in s1:
            need[ord(c)-97] += 1
        for r, c in enumerate(s2):
            win[ord(c)-97] += 1
            if r >= n:
                win[ord(s2[r-n])-97] -= 1
            if win == need:
                return True
        return False
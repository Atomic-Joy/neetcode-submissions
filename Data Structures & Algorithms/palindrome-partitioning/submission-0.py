class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def bt(i, path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                x = s[i:j+1]
                if x == x[::-1]:
                    path.append(x)
                    bt(j + 1, path)
                    path.pop()
        bt(0, [])
        return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res = []
        def bt(i, path):
            if i == len(digits):
                res.append(''.join(path))
                return
            for c in mp[digits[i]]:
                path.append(c)
                bt(i + 1, path)
                path.pop()
        bt(0, [])
        return res
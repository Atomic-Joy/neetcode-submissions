class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for x in path.split('/'):
            if x == '' or x == '.':
                continue
            if x == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/' + '/'.join(stack)
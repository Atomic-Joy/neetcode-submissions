class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            distance = grid[r][c] + 1
            if r + 1 < m and grid[r + 1][c] == INF:
                grid[r + 1][c] = distance
                q.append((r + 1, c))
            if r > 0 and grid[r - 1][c] == INF:
                grid[r - 1][c] = distance
                q.append((r - 1, c))
            if c + 1 < n and grid[r][c + 1] == INF:
                grid[r][c + 1] = distance
                q.append((r, c + 1))
            if c > 0 and grid[r][c - 1] == INF:
                grid[r][c - 1] = distance
                q.append((r, c - 1))
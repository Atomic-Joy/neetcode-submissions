class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            l, r = (l + 1, r) if height[l] < height[r] else (l, r - 1)
        return ans
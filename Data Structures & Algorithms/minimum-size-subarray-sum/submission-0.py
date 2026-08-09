class Solution:
    def minSubArrayLen(self, target, nums):
        l = total = ans = 0
        for r, x in enumerate(nums):
            total += x
            while total >= target:
                ans = min(ans or float('inf'), r - l + 1)
                total -= nums[l]
                l += 1
        return ans
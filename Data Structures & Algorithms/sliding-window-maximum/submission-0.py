class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q,res=[],[]
        for i,x in enumerate(nums):
            while q and q[0]<=i-k:q.pop(0)
            while q and nums[q[-1]]<=x:q.pop()
            q.append(i)
            if i>=k-1:res.append(nums[q[0]])
        return res
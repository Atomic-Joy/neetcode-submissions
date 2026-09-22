class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def bt(a):
            if len(a) == len(nums):
                res.add(tuple(a))
                return
            for x in nums:
                if x not in a or a.count(x) < nums.count(x):
                    bt(a + [x])
        bt([])
        return [list(x) for x in res]
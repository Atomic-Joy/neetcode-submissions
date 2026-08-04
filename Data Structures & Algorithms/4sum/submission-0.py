class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return list({
            quad for quad in combinations(nums, 4)
            if sum(quad) == target
        })
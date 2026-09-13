class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(remaining, start, current):
            if remaining == 0:
                result.append(current.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                current.append(nums[i])
                backtrack(remaining - nums[i], i, current)
                current.pop()

        backtrack(target, 0, [])
        return result
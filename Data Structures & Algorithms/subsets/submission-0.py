class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            backtrack(index + 1, current)
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()
        backtrack(0, [])
        return result
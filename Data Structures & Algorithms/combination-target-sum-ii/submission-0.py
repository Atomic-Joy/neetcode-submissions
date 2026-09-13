class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(remaining, start, current):
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1, current)
                current.pop()

        backtrack(target, 0, [])
        return result
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor |= num
        return xor * (1 << (len(nums) - 1))
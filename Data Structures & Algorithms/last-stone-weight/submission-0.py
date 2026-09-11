class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            x = stones.pop(0)
            y = stones.pop(0)
            if x != y:
                stones.append(x - y)
                stones.sort(reverse=True)
        return stones[0] if stones else 0
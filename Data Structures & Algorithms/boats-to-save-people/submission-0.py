class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r, ans = 0, len(people) - 1, 0
        while l <= r:
            l += people[l] + people[r] <= limit
            r -= 1
            ans += 1
        return ans
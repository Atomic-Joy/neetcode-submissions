class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and a < 0 < s[-1] and s[-1] < -a:
                s.pop()
            if not s or a > 0 or s[-1] < 0:
                s.append(a)
            elif s[-1] == -a:
                s.pop()
        return s
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for pos, spd in zip(position, speed):
            time = (target - pos) / spd
            cars.append((pos, time))
        cars.sort(reverse=True)
        fleets = 0
        slowest_time = 0
        for pos, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time
        return fleets
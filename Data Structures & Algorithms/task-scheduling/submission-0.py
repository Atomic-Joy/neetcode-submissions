class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        max_freq = 0
        for count in freq:
            max_freq = max(max_freq, count)
        max_count = 0
        for count in freq:
            if count == max_freq:
                max_count += 1
        intervals = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), intervals)
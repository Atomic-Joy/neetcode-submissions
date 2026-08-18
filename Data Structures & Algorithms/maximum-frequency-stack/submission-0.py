class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val):
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)
        self.maxFreq = max(self.maxFreq, f)

    def pop(self):
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
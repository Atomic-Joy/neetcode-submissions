class Solution:
    def findInMountainArray(self, target, arr):
        n = arr.length()
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if arr.get(m) < arr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l
        def search(l, r, asc):
            while l <= r:
                m = (l + r) // 2
                x = arr.get(m)
                if x == target:
                    return m
                if (x < target) == asc:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        return search(0, peak, True) if search(0, peak, True) != -1 \
               else search(peak + 1, n - 1, False)
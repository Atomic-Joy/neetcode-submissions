class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(a):
            if len(a) <= 1:
                return a
            m = len(a) // 2
            l = mergeSort(a[:m])
            r = mergeSort(a[m:])
            res = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i]); i += 1
                else:
                    res.append(r[j]); j += 1
            return res + l[i:] + r[j:]

        return mergeSort(nums)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if pos[x] != pos[y]:
                    if pos[x] > pos[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True
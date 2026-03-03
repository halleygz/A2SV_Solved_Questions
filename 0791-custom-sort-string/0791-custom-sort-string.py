class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = [ch*count[ch] for ch in order]

        res.extend(filter(lambda x: x not in order, s))

        return ''.join(res)
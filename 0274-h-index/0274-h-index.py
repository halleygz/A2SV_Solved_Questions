class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
        indexed = sorted(citations, reverse=True)

        hindex = 0

        for i in range(len(indexed) - 1):
            if indexed[i] < i + 1:
                break
            hindex += 1

        return hindex
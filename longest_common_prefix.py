class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        ordered = sorted(strs)
        first = ordered[0]
        last = ordered[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common
            common += first[i]
        return common
        
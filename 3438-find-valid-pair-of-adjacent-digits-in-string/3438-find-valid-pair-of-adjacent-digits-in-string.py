class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        res = "" # 2 1 2
        prev = "0" # 2 1 2

        # 212

        for num in s:
            if count[num] == int(num) and prev != num:
                res += num
                if len(res) == 2:
                    return res
                prev = num
            
        return res if len(res) >= 2 else ""
        
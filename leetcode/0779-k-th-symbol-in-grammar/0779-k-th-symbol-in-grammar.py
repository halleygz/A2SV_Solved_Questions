class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k <= 2:
            return k - 1
        return k % 2 if self.kthGrammar(n - 1, (k + 1) // 2) == 1 else (k + 1) % 2
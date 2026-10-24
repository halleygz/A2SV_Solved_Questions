class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2)
            res = (res * res ) % MOD
            return res  * x  if n % 2 else res

        odd = math.floor(n / 2)
        even = math.ceil(n / 2)
        MOD = 10**9 + 7


        return (helper(5, even) * helper(4, odd)) % MOD
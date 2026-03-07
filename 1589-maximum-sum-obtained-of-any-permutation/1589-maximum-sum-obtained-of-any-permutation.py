class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        count = count[:-1]
        nums.sort(reverse=True)
        count.sort(reverse=True)
        result = 0
        for i in range(n):
            result += count[i] * nums[i]
        return result % (10 ** 9 + 7)

        a.sort()
        nums.sort()
        ans=0
        N=1e9 + 7
        for i in range(n-1,-1,-1):
            ans+=(a[i]*nums[i])%N
            ans%=N
        return int(ans%N)
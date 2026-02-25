class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        C = [0] * 101

        for i in range(len(nums)):
            C[nums[i]] += 1
        P = [0] * 101
        for i in range(1, 101):
            P[i] = P[i - 1] + C[i -1]
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[i] = P[nums[i]]

        return res
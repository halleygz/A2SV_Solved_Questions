class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum(i for i in nums if i % 2 == 0)
        res = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sum_even -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                sum_even += nums[idx]

            res.append(sum_even)
        
        return res
        
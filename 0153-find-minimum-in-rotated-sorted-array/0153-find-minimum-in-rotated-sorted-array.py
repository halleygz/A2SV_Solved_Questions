class Solution:
    def findMin(self, nums: List[int]) -> int:
        size: int = len(nums)
        start: int = 0
        end: int = size - 1
        mini: int = nums[0]
        while start <= end:
            mid = start + (end - start) // 2

            if nums[start] <= nums[mid]:
                mini = min(nums[start], mini)
                start = mid + 1
            else:
                mini = min(nums[mid], mini)
                end = mid - 1

        return mini
        
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_hash = {0:-1}
        reminder = 0

        for i in range(len(nums)):
            reminder += nums[i]
            reminder %= k

            if reminder not in reminder_hash:
                reminder_hash[reminder] = i
            elif i - reminder_hash[reminder] >= 2:
                return True

        return False
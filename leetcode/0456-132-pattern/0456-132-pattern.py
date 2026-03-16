class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 3:
            return False
        
        decreasing = deque()

        max_third_el = float('-inf')

        for i in range(length - 1, -1, -1):
            current_number = nums[i]
            
            if current_number < max_third_el:
                return True
            
            while decreasing and decreasing[0] < current_number:
                max_third_el = decreasing.popleft()

            decreasing.appendleft(current_number)
        
        return False
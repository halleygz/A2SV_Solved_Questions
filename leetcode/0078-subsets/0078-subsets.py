class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Ans = []
        n = len(nums)

        # Helper function
        def Helper(op, start_index):
            # base case
            if start_index == n:
                Ans.append(list(op))
                return
            
            op.append(nums[start_index])
            Helper(op, start_index + 1)
            
            op.pop()
            
            Helper(op, start_index + 1)
        
        Helper([], 0)
        return Ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numsOfPaths = 0
        self.dfs(root, targetSum)

        return self.numsOfPaths
    def dfs(self, node, targetSum):
        if node is None:
            return
        self.test(node, targetSum)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)

    def test(self, node, targetSum):
        if node is None:
            return
        if node.val == targetSum:
            self.numsOfPaths += 1
        
        self.test(node.left, targetSum - node.val)
        self.test(node.right, targetSum - node.val)
        
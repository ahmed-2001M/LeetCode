# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0
        ans = 0
        
        def dfs(node,sm):
            if not node:
                return False
            sm+=node.val
            if not node.left and not node.right:
                return sm == targetSum
            
            return dfs(node.left,sm) or dfs(node.right , sm)
        
        return dfs(root ,0)
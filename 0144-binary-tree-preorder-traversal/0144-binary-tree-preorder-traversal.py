# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        def dfs(p: Optional[TreeNode]): 
            if not p:
                return
            ls.append(p.val)
            dfs(p.left)
            dfs(p.right)
        dfs(root)
        return ls
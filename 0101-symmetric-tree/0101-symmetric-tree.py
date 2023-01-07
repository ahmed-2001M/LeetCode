# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(p,q):
            if p ==None and q==None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            
            
            res=1
            res&=solve(p.left,q.right) & solve(p.right , q.left)
            return res
        return solve(root.left,root.right)
        
        
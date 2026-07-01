# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalancedCheck = True
        #DFS -> SubProblem -> Check left and right If abs(LEFT Height - RIGHT) height > 1 return false
        self.dfs(root)
        print(self.isBalancedCheck )

        return self.isBalancedCheck 
    
    def dfs(self, root) : 
        if self.isBalancedCheck == False : 
            return 0

        if root is None : 
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        print("node : ", root.val,"left : ", left,"right : ", right)
        if abs(left - right) > 1 : 
            print("False ",abs(left - right))
            self.isBalancedCheck =False
            return 0
        return 1 + max(left, right)
        
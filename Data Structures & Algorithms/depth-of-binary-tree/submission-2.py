# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #DFS 재귀의 개념 -> Problem - calculate the max length between left and right child
        #-> make it as subproblem


        if root is None : 
            return 0

        #level 1 > return 1
        

        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
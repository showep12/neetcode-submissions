# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Backtracking : If there is no answer, immediatly return
        path = []        
        def RecursiveBactracking(root, path, targetSum) : 
            if root is None : #if there is no child, return 
                return False
            print(path)
            path.append(root.val)

            if root.left is None and root.right is None : #if there is no child, return True, because we traversed to the leaf node
                if (sum(path) == targetSum) :
                    return True                

            if RecursiveBactracking(root.left, path, targetSum) : 
                return True

            if RecursiveBactracking(root.right, path, targetSum) : 
                return True

            path.pop()
            return False

        return RecursiveBactracking(root, path, targetSum)


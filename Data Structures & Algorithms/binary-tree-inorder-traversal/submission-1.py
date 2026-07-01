# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorder traversal means sorting the values
        #but this Binary tree doesn't have the sorted property,
        #even if I perform inorder traversal, the list can not be sorted

        #always if you reach a leaf node (which has no children), you gotta return null
        # print(root)
        answer = [] #global variable
        
        # self.inorderTraversal(root.left)          
        
        # self.inorderTraversal(root.right)

        #nested function
        def inorder(root) : 
            if (root is None) :
                return None
    
            inorder(root.left)
            answer.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return answer        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # print(root)
        if (root is None) :
            return root
        #when I reach a leaf (it has no children)
        #I go back to parent and invert the tree
        #
        print(root.right)
        print(root.left)

        #switch the leaf
        tempRight = root.right
        root.right = root.left
        root.left = tempRight

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



        print(root.right)
        print(root.left)
        
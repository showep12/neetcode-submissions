# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #finding the k-th smallest value in the tree (k is 1-indexed)

        #inorder traversal because we have to sort the tree's values
        #we 
        """
        Pattern : DFS and Inorder traversal / 
        Idea : 
        Invariant : 
        """
        stack = []
        sortedList = []
        curr = root

        while (curr) : #until there is no left child
                stack.append(curr) #append subtree itselft
                print(curr.val)
                curr = curr.left


        while (stack or curr) : 
            while (curr) : #until there is no left child
                stack.append(curr)  #append subtree itselft
                curr = curr.left
            
            #after left searching is finished, get back to the parent node, and search right direction
            curr = stack.pop()
            sortedList.append(curr.val)
            if (len(sortedList) == k) :
                return sortedList[k-1]
            curr = curr.right

            


        if (stack) : 
            print('a')
        return 0
        # if (root is None) : 
        #     return None
        # self.kthSmallest(root.left, k)
        # print(root.val)
        # self.kthSmallest(root.right, k)
        # return 0
        
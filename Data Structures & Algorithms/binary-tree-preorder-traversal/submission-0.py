# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Using Stack
        #1)print node first because root -> left -> right
        #2)Add right child to the stack, to visit later
        #3)check left child to visit
        #4)if left child exist -> go left node and repeat 1~4        
        #  else -> we checked node , left, now we check right (I mean stack I stored to visit)
        #          if visit right node, repeat 1~4 again
        #          else there is no to visit, return and check the stack again
        #          in else, we only check the stack until there are new 
        curr = root
        stack = []
        answer = []
        while (stack or curr) : #root until there are no nodes to newly visit  
            if curr : #1) if I visit new node
                answer.append(curr.val) #2) visit root first
                if curr.right is not None : #3) check the right child and add to the stack
                    stack.append(curr.right)
                curr = curr.left #4) visit left node continuously            
            else : #“If the current node is null , it means there are no left childs to check
                   # we have to check right child
                curr = stack.pop() #

        print(answer)
        return answer    


        


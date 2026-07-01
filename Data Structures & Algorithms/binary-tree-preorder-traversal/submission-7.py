# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #PreOrder Traversal -> Root -> Left -> Right
        #Process current First, 

        #Visit Node, Add Right / Left to Stack
        #pop the left node, check whether it has child
        #go to the child, add to the stack

        curr = root
        answer = []
        stack = []        
        
        while (stack or curr is not None) : #시작점이거나, stack에 
            if curr : 
                answer.append(curr.val)                        
                print("Visit - " + str(curr.val))

            # print(curr.val) 
            # print(stack)

            if curr.right is not None : 
                stack.append(curr.right)
                print("Right - " + str(curr.right.val))
            if curr.left is not None : 
                stack.append(curr.left)
                print("Left - " + str(curr.left.val))                        
            # print(answer)
            if (stack) : 
                next = stack.pop() #left 먼저
                curr = next
            else : 
                curr = None
            
            

        return answer


            



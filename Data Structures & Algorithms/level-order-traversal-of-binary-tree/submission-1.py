# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        queue = deque() 
        #popleft
        #pop
        #appendleft
        #append

        if (root is None) : 
            return answer
        else :
            queue.append(root)
            subList = [root.val]
            answer.append(subList)
            print(subList)
            level = 1

            while (len(queue) > 0) : #

                #remove first node from search target List
                # curr = queue.popleft() #left is first
                
                print("level : " + str(level))
                level += 1
                for i in range(len(queue)) :
                    curr = queue.popleft() #left is first                       
                    if curr.left : 
                        queue.append(curr.left)
                        print(curr.left.val)
                    if curr.right : 
                        queue.append(curr.right)
                        print(curr.right.val)
                subList = []                    
                for tree in queue :
                    # print(tree.val) 
                    subList.append(tree.val)
                if (len(subList) > 0) : 
                    answer.append(subList)
                # print(subList)





            return answer
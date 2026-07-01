# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #maximum node counts : 100
        #for each level, find the rightmost value
        #make sublist of each level, and choose the rightmost value

        queue = deque()
        answer = []
        if queue : 
            print(True)
        if root is None : 
            return []
        
        queue.append(root)
        answer.append(root.val)
        level = 1
            

        while queue : #if there are next children in current level
            print("level " + str(level)) 
            print(queue)
            for i in range(len(queue)) : #each level, traverse every nodes in the same level
                curr = queue.popleft()                                
                if curr.left : 
                    queue.append(curr.left)            
                    print(curr.left.val)
                if curr.right : 
                    queue.append(curr.right)
                    print(curr.right.val)                        
            
            if (len(queue) > 0) : 
                rightmost = queue[-1]
                answer.append(rightmost.val)
            print(answer)
            # answer.append(sublist.pop())
            
        return answer



        

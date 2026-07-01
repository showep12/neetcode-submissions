# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #This is not the binary search tree, this is just a binary tree it means it can not 

        #actually 
        print(root)
        if root is None : 
            return 0
        #inorder
        #preorder
        #postorder
        queue = deque()
        queue.append(root)

        level = 0
        while queue : 
            level += 1
            print(level)
            print(queue)
            for i in range(len(queue)) : #even if the queue is changed, the iteration times does not change
                curr = queue.popleft()
                
                if curr.left : 
                    queue.append(curr.left)

                if curr.right : 
                    queue.append(curr.right)

        return level

        # a = deque([1,2])
        # a.popleft()
        # a.appendleft('d') #appendleft - pop  / popleft - append
        # print(a)

        #we have to use bfs becuase we have to know the depth

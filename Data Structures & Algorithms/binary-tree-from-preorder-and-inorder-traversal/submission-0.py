# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not preorder or not inorder) : 
                return None

        root = TreeNode(preorder[0])  #beginning of node - rootnode
        mid = inorder.index(preorder[0]) #rootnode's position in inorder List
        #it means that left elements from the rootnode's index is more lowerleft position 
        #It means the elements to the left of the root’s index in the inorder 
        #   array belong to the root’s left subtree.
        #if there are 3 elements exist, it means root have subtree of size 3
        #it means in the preorder, they just neet to visit 3 count, not all

        print(preorder, inorder)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

        
        #preorder traversal means visiting order
        #inorder traversal means sorting order
        #postorder traversal means children firest order
        
        #building a BST from a List
        #Inorder = Left → Node → Right (정의 자체가 left first)
        #Preorder = Node → Left → Right
        #Postorder = Left → Right → Node

        #Inorder traversal is just a visiting order (left → node → right). 
        #It produces sorted output only for a valid BST.


        #visit preorder, and if there is left values inorder List,
        #it means there are still remained values to 

          
        # print(node.val)
        # print(node.left)
# “In the current inorder segment, if there are still elements to the left of the root’s index, 
#that exactly means the left subtree hasn’t been built yet—so I build the left subtree first.”
        """
        “Preorder tells me the root of the current subtree because 
        it’s root-first. Once I pick the root, I locate it in the inorder array; 
        everything left of that index belongs to the left subtree, 
        and everything right belongs to the right subtree. Since preorder is root–left–right, 
        I recursively build the left subtree first, then the right subtree. 
        With a hashmap from value to inorder index, the overall time is O(n).”
        """
        #1. Create root
        #2. check there is left values exist in the inorderList
        #3. if exist > make left child, keep going
        #4. if doesn't, end making left and go back to the parent
        #5. and if there is no left elements, it is root node
        #6. 

        
        
       

# “I treat this as a divide-and-conquer reconstruction. I maintain an invariant: in each recursive call, the inorder range [L..R] represents exactly the nodes in the subtree I’m building, and a preorder pointer gives me the next root. I take preorder[pre_i] as the root, then use a map to find its position mid in inorder. If mid > L, that means there are nodes on the left side of the root within this inorder range, so a left subtree exists and I build it first. The size of the left subtree is mid - L, which determines how the preorder pointer advances naturally as recursion proceeds. After finishing the left subtree, I build the right subtree from [mid+1..R]. This visits each node once, so time is O(n), and space is O(n) for the map plus O(h) for the recursion stack.”

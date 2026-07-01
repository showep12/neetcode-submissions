# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #1-> 2-> 4
        #2 -> 3 -> 4

        #sorted linked list
        #change the next node

        #list 1 curr node
        #list 2 curr node
        #-> compare two nodes' value and choose the small one
        #small one's next node 
        #-> compare the not chosen node and the chosen node's next value
        #-> set next node of current chosen node
        #-> 

        #-> end these 
        curr_node_list1 = list1
        curr_node_list2 = list2
        head = ListNode()
        new_node = head

        while curr_node_list1 and curr_node_list2 : 
            prev_node = None
            next_node = None
            if curr_node_list1.val <= curr_node_list2.val : 
                prev_node = curr_node_list1 
                curr_node_list1 = curr_node_list1.next
            else : 
                prev_node = curr_node_list2
                curr_node_list2 = curr_node_list2.next

            new_node.next = prev_node
            new_node = prev_node

        if curr_node_list1 : 
            new_node.next = curr_node_list1
        
        if curr_node_list2 : 
            new_node.next = curr_node_list2
            

        
        return head.next